from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

with DAG('remove_logs_folders', schedule_interval=timedelta(days=1), start_date=days_ago(1)) as dag:
    t1 = BashOperator(task_id='remove_logs_folders', bash_command='rm -r $AIRFLOW_HOME/logs/')
