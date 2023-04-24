from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.models import BaseOperator
from random import randint


class DummyOperator(BaseOperator):
    ui_color = '#e8f7e4'

    # inherits_from_dummy_operator = True

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, context):
        context['ti'].xcom_push(key='rand', value=randint(0, 10))


dag = DAG('random_push_xcom', schedule_interval='@daily', start_date=days_ago(1))
t1 = DummyOperator(task_id='task_1', dag=dag)
t2 = DummyOperator(task_id='task_2', dag=dag)

t1 >> t2
