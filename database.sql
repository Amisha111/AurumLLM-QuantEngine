DROP TABLE IF EXISTS commodity_market_warehouse;

CREATE TABLE commodity_market_warehouse (
    trade_date DATE PRIMARY KEY,
    closing_price NUMERIC,
    opening_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    trading_volume NUMERIC,
    daily_percentage_change NUMERIC,
    price_lag_1 NUMERIC,
    sma_5 NUMERIC,
    sma_20 NUMERIC,
    rolling_volatility_5 NUMERIC,
    predicted_next_day_price NUMERIC,
    tracking_residual NUMERIC
);
