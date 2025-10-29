WITH base AS (
    SELECT * FROM "customer_churn_warehouse"."analytics"."staging_customer_churn"
)
SELECT
    gender,
    Contract,
    InternetService,
    COUNT(*) AS total_customers,
    SUM(Churn_Flag) AS churned_customers,
    ROUND(SUM(Churn_Flag) * 100.0 / COUNT(*), 2) AS churn_rate
FROM base
GROUP BY 1,2,3
ORDER BY churn_rate DESC