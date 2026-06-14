import pandas as pd
import numpy as np

def generate_financial_indicators(df):
    print("Transforming underlying financial dimensions and extracting market signals...")
    df = df.copy()
    
    # 1. Capture strict past-day indicators to prevent lookahead target leakage
    df['price_t_minus_1'] = df['Price'].shift(1)
    df['open_t_minus_1'] = df['Open'].shift(1)
    df['high_t_minus_1'] = df['High'].shift(1)
    df['low_t_minus_1'] = df['Low'].shift(1)
    df['volume_t_minus_1'] = df['Volume'].shift(1)
    df['chg_t_minus_1'] = df['Chg%'].shift(1)
    
    # 2. Derive technical oscillators and trend-following signals
    df['sma_5'] = df['Price'].shift(1).rolling(window=5).mean()
    df['sma_20'] = df['Price'].shift(1).rolling(window=20).mean()
    df['rolling_vol_5'] = df['Price'].shift(1).rolling(window=5).std()
    
    df = df.dropna().reset_index(drop=True)
    df.to_csv("data/processed/gold_features_transformed.csv", index=False)
    return df
