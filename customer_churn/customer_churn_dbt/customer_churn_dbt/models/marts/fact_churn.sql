WITH base AS (
    SELECT * FROM {{ ref('staging_customer_churn') }}
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
