from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'mahmoud',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='churn_pipeline_dag',
    default_args=default_args,
    description='ETL pipeline: MySQL -> DuckDB -> dbt',
    schedule_interval='@daily',  # تشغيل يومي
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['customer_churn', 'data_pipeline'],
) as dag:

    # 1️⃣ تحميل البيانات من CSV إلى MySQL
    load_mysql = BashOperator(
        task_id='load_to_mysql',
        bash_command='python /path/to/project/src/load_to_mysql.py'
    )

    # 2️⃣ نقل البيانات من MySQL إلى DuckDB
    mysql_to_duckdb = BashOperator(
        task_id='mysql_to_duckdb',
        bash_command='python /path/to/project/src/mysql_to_duckdb.py'
    )

    # 3️⃣ تشغيل dbt للتحويل داخل DuckDB
    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /path/to/project/customer_churn_dbt && dbt run'
    )

    # تسلسل التشغيل
    load_mysql >> mysql_to_duckdb >> run_dbt
