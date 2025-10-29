import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='302112',
            database='customer_churn_db'
        )
        if connection.is_connected():
            print("✅ Connected to MySQL successfully!")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None

def load_csv_to_mysql(csv_path):
    # اقرأ البيانات
    df = pd.read_csv(csv_path)
    print(f"📦 Loaded {len(df)} rows from {csv_path}")

    conn = create_connection()
    if conn is None:
        return
    
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO customer_churn (
            customerID, gender, SeniorCitizen, Partner, Dependents,
            tenure, PhoneService, MultipleLines, InternetService,
            OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
            StreamingTV, StreamingMovies, Contract, PaperlessBilling,
            PaymentMethod, MonthlyCharges, TotalCharges, Churn
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():
        data = tuple(row)
        try:
            cursor.execute(insert_query, data)
        except Error as e:
            print(f"⚠️ Skipped row due to error: {e}")

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data inserted successfully into MySQL!")

if __name__ == "__main__":
    load_csv_to_mysql("data/customer_churn.csv")
