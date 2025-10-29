
  
  create view "customer_churn_warehouse"."analytics"."staging_customer_churn__dbt_tmp" as (
    WITH source AS (
    SELECT * FROM staging.customer_churn
)
, cleaned AS (
    SELECT
        customerID AS customer_id,
        gender,
        SeniorCitizen,
        Partner_Flag,
        Dependents_Flag,
        tenure,
        InternetService,
        Contract,
        MonthlyCharges,
        TotalCharges,
        Churn_Flag
    FROM source
)
SELECT * FROM cleaned
  );
