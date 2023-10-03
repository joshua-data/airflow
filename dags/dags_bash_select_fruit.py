# Import Libraries

import datetime, pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

# Define DAG

with DAG(
    dag_id = 'dags_bash_select_fruit',
    schedule = '10 0 * * 6#1', # 매월 1번째 토요일 0시 10분
    start_date = pendulum.datetime(2023, 9, 1, tz='Asia/Seoul'),
    catchup = False,
) as dag:
    
    t1_orange = BashOperator(
        task_id = 't1_orange',
        bash_command = '/opt/airflow/plugins/shell/select_fruit.sh ORANGE',
    )

    t2_apple = BashOperator(
        task_id = 't2_apple',
        bash_command = '/opt/airflow/plugins/shell/select_fruit.sh APPLE',
    )

    t3_avocado = BashOperator(
        task_id = 't3_avocado',
        bash_command = '/opt/airflow/plugins/shell/select_fruit.sh AVOCADO',
    )

    t1_orange >> t2_apple >> t3_avocado