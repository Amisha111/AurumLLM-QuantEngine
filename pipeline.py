import os
import pandas as pd

def run_ingestion_pipeline(file_path="Gold Price.csv"):
    print("Beginning structural ingestion and market closure patching...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing base resource file: {file_path}")
        
    df = pd.read_csv(file_path)
    df.columns = [col.strip() for col in df.columns]
    
    # Enforce strict datetime structure and sequential timeline order
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date').reset_index(drop=True)
    
    # Correct calendar/holiday trading gaps through step forward-filling
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].ffill().bfill()
    
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/gold_base_cleaned.csv", index=False)
    print("Base cleaning complete. Output saved to data/processed/gold_base_cleaned.csv")
    return df

if __name__ == "__main__":
    run_ingestion_pipeline()
