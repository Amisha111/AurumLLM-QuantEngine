# AurumLLM-QuantEngine
AurumLLM-QuantEngine is an end-to-end Python, SQL, and ML asset forecasting system tracking bullion values. It features a relational SQLite database for market trend analysis, addresses ensemble model extrapolation breakdowns using Ridge Regression ($0.9982\ R^2$), and embeds a Gen AI agent for automated strategic advisory commentary.
AurumLLM-QuantEngine/
│
├── data/
│   ├── raw/                  # Place the raw Gold Price.csv file here
│   └── processed/            # Holds gold_features_transformed.csv after running pipeline
│
├── database/
│   ├── schema.sql            # Table structure for structured financial data warehousing
│   └── analytical_queries.sql# SQL scripts for computing asset returns and rolling parameters
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py      # Cleans, validates dates, and handles forward-fills
│   ├── feature_engineering.py# Computes lags, momentum indicators, and technical oscillators
│   ├── train.py              # Compares tree models vs. regularized linear learners
│   ├── gen_ai_agent.py       # Core Gen AI financial agent generating commentary and RAG context
│   └── visualize.py          # Programmatic script to render high-resolution performance plots
│
├── notebooks/                # Saved charts and analytical telemetry report figures
│   ├── actual_vs_forecasted_gold_ridge.png
│   ├── market_feature_importance_gold.png
│   └── error_residual_analysis.png
│
├── requirements.txt          # Absolute library dependencies
└── README.md                 # Complete, non-emoji portfolio documentation


