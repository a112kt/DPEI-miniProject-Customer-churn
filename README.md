📄 README — Customer Churn Reporting & Visualization Platform

## 🎥 Demo Video


🔗 [اضغط هنا لمشاهدة الفيديو على Google Drive](https://drive.google.com/file/d/1bJ5uq-vqKlLI7HIEcKcDXonw5XNYD5d4/view?usp=drive_link)


📌 Project Name:
Customer Churn Reporting & Visualization Platform

📌 Track:
Data Engineering — DEPI

✅ Objective
This project implements a complete end-to-end data engineering pipeline to analyze and understand customer churn behavior for a telecom company.

It covers the full data lifecycle:

Data ingestion from MySQL

Analytical warehousing using DuckDB

Data transformation & modeling with dbt

Workflow automation using Apache Airflow

Interactive visualization using Dash & Plotly

🏗️ 1. Environment Setup Guide

Below is the list of required tools and installation instructions.

Tool	Purpose	Installation
Python ≥ 3.9	Main programming language	python.org/downloads
MySQL Server	Transactional source database	dev.mysql.com/downloads/mysql
DuckDB	Analytical local data warehouse	pip install duckdb
Apache Airflow	Pipeline orchestration	pip install apache-airflow
dbt-duckdb	Data transformation & modeling	pip install dbt-core dbt-duckdb
Dash & Plotly	Visualization	pip install dash plotly
Pandas	Data manipulation	pip install pandas
MySQL Connector	Python ↔ MySQL connection	pip install mysql-connector-python
📁 2. Project Structure
Project_Customer_Churn_Reporting__Visualization_Platform/
│
├─ data/
│   ├─ customer_churn.csv
│   ├─ customer_churn_warehouse.duckdb
│
├─ sql/
│   └─ schema.sql
│
├─ src/
│   ├─ data_generator.py
│   ├─ load_to_mysql.py
│   ├─ mysql_to_duckdb.py
│   ├─ db.py
│   ├─ etl.py
│   ├─ plotly_report.py
│   ├─ app_dash.py
│
├─ customer_churn_dbt/
│   ├─ dbt_project.yml
│   ├─ models/
│   │   ├─ staging/
│   │   │   ├─ staging_customer_churn.sql
│   │   │   └─ staging_customer_churn.yml
│   │   ├─ intermediate/
│   │   │   └─ intermediate_customer_metrics.sql
│   │   ├─ marts/
│   │   │   └─ fact_churn.sql
│
├─ airflow_dags/
│   └─ churn_pipeline_dag.py
│
├─ docs/
│   └─ Technical_Documentation_Customer_Churn.pdf
│
├─ outputs/
│   └─ churn_report.html
│
└─ README.md

🔐 3. Environment Configuration (.env)

Create a .env file in the root directory:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=customer_churn_db

DUCKDB_PATH=./data/customer_churn_warehouse.duckdb

🧱 4. Architecture Overview

The pipeline has five functional layers:

✅ 1. Data Ingestion Layer

Load CSV into MySQL using Python and Pandas.

✅ 2. Data Warehousing Layer

Migrate data from MySQL → DuckDB for analytical queries.

✅ 3. Transformation Layer

Use dbt for:

Transformations

Testing

Documentation

Model lineage

✅ 4. Orchestration Layer

Airflow automates:

ETL tasks

dbt runs

Daily scheduled pipelines

✅ 5. Visualization Layer

A Dash + Plotly dashboard connects to DuckDB for interactive charts.

📊 5. Documentation & Diagrams

The project includes:

Data Flow Diagram:
Shows movement from CSV → MySQL → DuckDB → dbt → Dash.

ERD:
Star schema:

fact_churn

dim_customer

dim_service

dim_geography

dbt Model Lineage:
Visualization of staging → intermediate → mart dependencies.

Setup Guide & Architecture Overview
Included in /docs/Technical_Documentation_Customer_Churn.pdf

✅ 6. Conclusion

This project demonstrates a complete and scalable data engineering pipeline using:

Python & Pandas for ingestion

MySQL for transactional storage

DuckDB as a local data warehouse

dbt for data modeling

Airflow for orchestration

Dash for visualization

It provides a reproducible workflow for telecom churn analysis and reflects the skills taught in the DEPI Data Engineering track.
