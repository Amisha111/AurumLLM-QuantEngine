-- Query 1: Extract Historical Volatility Regimes and Moving Average Spreads
SELECT 
    trade_date,
    closing_price,
    sma_5,
    sma_20,
    (sma_5 - sma_20) AS ma_crossover_spread,
    rolling_volatility_5,
    CASE 
        WHEN rolling_volatility_5 > (SELECT AVG(rolling_volatility_5) FROM commodity_market_warehouse) * 1.5 THEN 'HIGH VOLATILITY REGIME'
        ELSE 'STABLE TRADING REGIME'
    END AS risk_state
FROM commodity_market_warehouse
WHERE trade_date >= '2024-01-01'
ORDER BY trade_date ASC;
