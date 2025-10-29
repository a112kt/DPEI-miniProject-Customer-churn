import mysql.connector
import pandas as pd
import duckdb

# 🔹 إعداد الاتصال بقاعدة MySQL
def extract_from_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='302112',
        database='customer_churn_db'
    )
    query = "SELECT * FROM customer_churn;"
    df = pd.read_sql(query, connection)
    connection.close()
    print(f"✅ Extracted {len(df)} rows from MySQL.")
    return df

# 🔹 تنظيف وتحويل البيانات
def transform_data(df):
    # مثال بسيط: نحول "Yes"/"No" إلى 1/0
    df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df['Partner_Flag'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Dependents_Flag'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    print("🧹 Data transformed successfully.")
    return df

# 🔹 تحميل البيانات إلى DuckDB
def load_to_duckdb(df):
    con = duckdb.connect("data/customer_churn_warehouse.duckdb")
    con.execute("CREATE SCHEMA IF NOT EXISTS staging;")
    con.execute("DROP TABLE IF EXISTS staging.customer_churn;")
    con.execute("CREATE TABLE staging.customer_churn AS SELECT * FROM df;")
    print("📦 Data loaded into DuckDB (schema: staging.customer_churn)")
    result = con.execute("SELECT COUNT(*) FROM staging.customer_churn;").fetchone()
    print(f"✅ DuckDB table created with {result[0]} rows.")
    con.close()

def main():
    df = extract_from_mysql()
    df = transform_data(df)
    load_to_duckdb(df)

if __name__ == "__main__":
    main()
