import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def run_backtest_simulation():
    print("Executing model optimization and chronological cross-validation splits...")
    df = pd.read_csv("data/processed/gold_features_transformed.csv")
    
    features = ['price_t_minus_1', 'open_t_minus_1', 'high_t_minus_1', 'low_t_minus_1', 'volume_t_minus_1', 'chg_t_minus_1', 'sma_5', 'sma_20', 'rolling_vol_5']
    X = df[features]
    y = df['Price']
    
    # CRITICAL IN SIGHT: Enforce strict time-ordered split (No random K-Fold data leakage)
    split_idx = int(len(df) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
    
    # Train robust linear model capable of handling price trend extrapolation
    model_ridge = Ridge(alpha=1.0)
    model_ridge.fit(X_train, y_train)
    preds_ridge = model_ridge.predict(X_test)
    
    print("\n==================================================")
    print("QUANT ENGINE TRACKING telemetry ERRORS")
    print("==================================================")
    print(f"Mean Absolute Error (MAE):     ${mean_absolute_error(y_test, preds_ridge):.2f} INR")
    print(f"Variance Captured (R2 Score):  {r2_score(y_test, preds_ridge):.4f}")
    print("==================================================\n")
    
    return model_ridge, X_test, y_test, preds_ridge

if __name__ == "__main__":
    run_backtest_simulation()
