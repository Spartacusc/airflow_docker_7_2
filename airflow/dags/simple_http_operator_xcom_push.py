from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago

from airflow.operators.http_operator import SimpleHttpOperator

with DAG('simple_http_operator', schedule_interval=timedelta(days=1), start_date=days_ago(1)) as dag:
    task = SimpleHttpOperator(
        task_id='simple_http_operator',
        method="get",
        http_conn_id='random_api',
        endpoint='?num=1&min=1&max=5&col=1&base=2&format=plain',
        xcom_push=True
    )
