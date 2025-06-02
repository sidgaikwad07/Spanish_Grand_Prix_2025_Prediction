# Spanish_Grand_Prix_2025_Prediction

🏎️ Spanish GP 2025 – F1 Race Prediction Models (Practice-Based)

Welcome to the Spanish Grand Prix 2025 Prediction Project, where we build two different models to predict race outcomes using only practice session data (FP1–FP3).
This repo showcases the power of combining machine learning with domain logic in Formula 1 sports analytics.

⚙️ Model 1: XGBoost Practice-Based Predictor
📌 Description
A machine learning model trained on historic race data (2021–2024), then used to predict the 2025 Spanish GP results based on:
Real FP1–FP3 data
Imputed missing values
Aligned training/testing feature distributions
📊 Highlights
MAE ≈ 0.22
Predicts finishing position for all 20 drivers
Learns from historical trends + performance patterns

🤖 Model 2: Realistic Logic-Based Grid Evaluator
📌 Description
A handcrafted Python pipeline that:
Models the 2025 driver grid changes
Scores drivers on: best lap, long-run pace, progression, consistency
Includes track-specific modifiers (e.g., Verstappen’s Spanish GP dominance)
🎯 Unique Features
Driver ratings from 2025 form
Team strength multipliers
Custom scoring formula with bonuses for home drivers & legends

🧠 Why Two Models?

XGBoost Model	 
 - Learns from historical finish data
 - Data-driven
 - Objective

Realistic Grid Logic
- Adapts to 2025 grid realities
- Domain-enhanced
- Human-intuition based
Combining both yields deeper insight into F1 race outcome forecasting.

🔗 Tools & Libraries

FastF1: Telemetry + session data (FP1–FP3)
XGBoost: Race outcome regression
Pandas, NumPy, Matplotlib: Analysis + Visualization
scikit-learn: Data imputation + preprocessing
📍 Key Takeaways

Max Verstappen, Lando Norris, and Lewis Hamilton appear as top contenders in both models.
The XGBoost model tends to favor historically strong teams.
The Realistic model highlights 2025 dynamics like rookie drivers and driver-team switches.

Visuals
Model 1 Predictions
![Prediction Visualization](https://drive.google.com/uc?export=view&id=1B4IGEbsBh0IEgs0090LKaGlurQ5JpsBt)

Model 2 Predictions
![Podium Prediction](https://drive.google.com/uc?export=view&id=1089BQGoF8GIfPzJy94kWyfHGvQPpVX33)
