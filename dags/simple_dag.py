from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print("Hello From Airflow!")


def goodbye():
    print("Goodbye From Airflow!")


with DAG(
    dag_id="simple_dag",
    start_date=datetime(2025, 5, 5),
    schedule="@daily",
    catchup=False,
) as dag:

    task1 = PythonOperator(task_id="print_hello", python_callable=print_hello)

    task2 = PythonOperator(task_id="goodbye", python_callable=goodbye)

    task1 >> task2
