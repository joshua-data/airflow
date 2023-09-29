# Import Libraries

import datetime, pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

# Define DAG

with DAG(
    dag_id = 'dags_bash_operator', # Recommended to be same with This File Name
    schedule = '0 0 * * *', # MIN / HOUR / DAY / MONTH / DoW
    start_date = pendulum.datetime(2023, 9, 1, tz='Asia/Seoul'),
    catchup = False, # If it needs to run the DAG for the missing interval. (starting from start_date to current date)
    dagrun_timeout = datetime.timedelta(minutes = 60), # Fail to run DAG if it spends more than 60 mins. 
    tags = ['example', 'example2'],
    params = {
        'example_key': 'example_value'
    }, # Common Params for Each Task Written Below.
) as dag:
    
    bash_t1 = BashOperator(
        task_id = 'bash_t1', # Recommended to be same with This Variable Name
        bash_command = 'echo whoami', # Print 'whoami'
    )

    bash_t2 = BashOperator(
        task_id = 'bash_t2',
        bash_command = 'echo $HOSTNAME', # Print $HOSTNAME
    )

    bash_t1 >> bash_t2
