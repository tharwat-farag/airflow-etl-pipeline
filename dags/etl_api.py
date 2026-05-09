from airflow import DAG
from datetime import datetime
import requests
import json

with DAG(
    dag_id="Api_etl_dag",
    start_date=datetime(2025, 5, 5),
    schedule="@daily",
    catchup=False,
) as dag:

    def extract():
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        data = response.json()
        print("extracted data:", data)
        return data

    def transform(ti):
        data = ti.xcom_pull(task_ids="extract_data")
        data["title"] = data["title"].upper()
        print("transformation completed", data)
        return data

    def load(ti):
        data = ti.xcom_pull(task_ids="transform_data")
        with open("/tmp/api_output.json", "w") as f:
            json.dump(data, f)

    task1 = PythonOperator(task_id="extract_data", python_callable=extract)

    task2 = PythonOperator(task_id="transform_data", python_callable=transform)

    task3 = PythonOperator(task_id="load_data", python_callable=load)

    task1 >> task2 >> task3
