"""
Created on Thu May 29 11:17:43 2025

@author: sid
Combining the clean data of the year 2024 and 2025
"""
import pandas as pd

# === File paths ===
FILE_2024 = "final_cleaned_2024_data.csv"
FILE_2025 = "final_cleaned_2025_data.csv"
OUTPUT_FILE = "combined_cleaned_2024_2025_with_positions.csv"

# === Load datasets ===
df_2024 = pd.read_csv(FILE_2024)
df_2025 = pd.read_csv(FILE_2025)

# === Add Year columns if missing (safety) ===
if "Year" not in df_2024.columns:
    df_2024["Year"] = 2024
if "Year" not in df_2025.columns:
    df_2025["Year"] = 2025

# === Align columns ===
common_columns = list(set(df_2024.columns) & set(df_2025.columns))
df_2024 = df_2024[common_columns]
df_2025 = df_2025[common_columns]

# === Concatenate ===
combined_df = pd.concat([df_2024, df_2025], ignore_index=True)

# === Export to CSV ===
combined_df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Combined dataset saved to: {OUTPUT_FILE}")