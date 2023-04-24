from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.models import Variable


def extract_login_and_password(**context):
    connection = BaseHook.get_connection("custom_conn_id")
    host = connection.host
    password = connection.password
    login = connection.login
    print(host, login, password)
    Variable.set(
        key="var", value={'host': host,
                          'login': login,
                          'password': password
                          }, serialize_json=True
    )


with DAG(dag_id='extract_login_and_password',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
         ) as dag:
    extract_data = PythonOperator(
        task_id='extract_data',
        python_callable=extract_login_and_password
    )
