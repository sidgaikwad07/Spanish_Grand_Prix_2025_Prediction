"""
Created on Thu May 29 08:57:11 2025

@author: sid
Updated script for 2024 F1 season data processing.
Enhancements:
- Adds session type (FP, Q, R, S)
- Merges driver Position from results.csv
- Prepares clean data for race/qualifying performance analysis
"""

import os
import pandas as pd
import numpy as np

# === Setup ===
RAW_DATA_DIR = "/Users/sid/Downloads/F1_FuturePrediction_2025/data_fetching"
OUTPUT_FILE = "/Users/sid/Downloads/Spanish_GP_2025/clean_data/final_cleaned_2024_data.csv"
YEAR_FILTER = "2024"

# === Initialize ===
all_sessions = []
race_positions = []
quali_positions = []

# === Loop through 2024 sessions only ===
for folder in sorted(os.listdir(RAW_DATA_DIR)):
    if not folder.startswith(YEAR_FILTER):
        continue

    session_path = os.path.join(RAW_DATA_DIR, folder)
    if not os.path.isdir(session_path):
        continue

    # Expected file paths
    laps_path = os.path.join(session_path, "laps.csv")
    results_path = os.path.join(session_path, "results.csv")
    weather_path = os.path.join(session_path, "weather.csv")

    if not os.path.exists(laps_path):
        print(f"⚠️ Skipping {folder}: No laps.csv")
        continue

    try:
        # Load laps
        laps_df = pd.read_csv(laps_path)
        if laps_df.empty or "LapTime" not in laps_df.columns:
            print(f"⚠️ Skipping {folder}: Invalid or empty laps.csv")
            continue

        # Basic cleanup
        laps_df["LapTimeSeconds"] = pd.to_timedelta(laps_df["LapTime"], errors='coerce').dt.total_seconds()
        laps_df = laps_df.dropna(subset=["LapTimeSeconds"])
        laps_df = laps_df[(laps_df["LapTimeSeconds"] > 40) & (laps_df["LapTimeSeconds"] < 200)]
        laps_df["SessionFolder"] = folder
        laps_df["Year"] = YEAR_FILTER

        # Determine session type
        if "_R" in folder:
            laps_df["SessionType"] = "Race"
        elif "_Q" in folder:
            laps_df["SessionType"] = "Qualifying"
        else:
            laps_df["SessionType"] = "Other"

        # Merge results to get final positions
        if os.path.exists(results_path):
            results_df = pd.read_csv(results_path)
            if "Abbreviation" in results_df.columns and "Position" in results_df.columns:
                results_df = results_df.rename(columns={"Abbreviation": "Driver"})
                if "_R" in folder:
                    results_df = results_df.rename(columns={"Position": "FinalRacePosition"})
                    race_positions.append(results_df[["Driver", "FinalRacePosition"]])
                elif "_Q" in folder:
                    results_df = results_df.rename(columns={"Position": "FinalQualiPosition"})
                    quali_positions.append(results_df[["Driver", "FinalQualiPosition"]])
                laps_df = laps_df.merge(results_df, on="Driver", how="left")

        # Merge average weather if available
        if os.path.exists(weather_path):
            weather_df = pd.read_csv(weather_path)
            if "AirTemp" in weather_df.columns:
                avg_temp = weather_df["AirTemp"].mean()
                laps_df["AvgAirTemp"] = avg_temp

        all_sessions.append(laps_df)
        print(f"✅ Processed {folder}, {len(laps_df)} valid laps")

    except Exception as e:
        print(f" Error processing {folder}: {e}")

# === Final assembly ===
if all_sessions:
    final_df = pd.concat(all_sessions, ignore_index=True)

    # Compute average finishing positions
    if race_positions:
        race_all = pd.concat(race_positions)
        race_all["FinalRacePosition"] = pd.to_numeric(race_all["FinalRacePosition"], errors='coerce')
        race_avg = race_all.groupby("Driver")["FinalRacePosition"].mean().rename("AvgRaceFinish")
        final_df = final_df.merge(race_avg, on="Driver", how="left")

    if quali_positions:
        quali_all = pd.concat(quali_positions)
        quali_all["FinalQualiPosition"] = pd.to_numeric(quali_all["FinalQualiPosition"], errors='coerce')
        quali_avg = quali_all.groupby("Driver")["FinalQualiPosition"].mean().rename("AvgQualiPosition")
        final_df = final_df.merge(quali_avg, on="Driver", how="left")

    final_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n📁 Final 2024 data saved to: {OUTPUT_FILE}")
else:
    print(" No valid 2024 session data processed.")