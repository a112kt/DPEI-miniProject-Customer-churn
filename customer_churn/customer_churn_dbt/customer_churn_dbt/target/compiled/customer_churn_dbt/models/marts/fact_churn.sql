WITH base AS (
    SELECT * FROM "customer_churn_warehouse"."analytics"."staging_customer_churn"
)
SELECT
    customer_id,
    tenure,
    Contract,
    InternetService,
    MonthlyCharges,
    TotalCharges,
    Churn_Flag
FROM base