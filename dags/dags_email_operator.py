# Import Libraries

import datetime, pendulum

from airflow import DAG
from airflow.operators.email import EmailOperator

# Define DAG

with DAG(
    dag_id = 'dags_email_operator',
    schedule = '0 8 1 * *',
    start_date = pendulum.datetime(2023, 9, 1, tz='Asia/Seoul'),
    catchup = False,
) as dag:
    
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = ['joshuajkim413@gmail.com', 'joshuajkim413eng@gmail.com'],
        subject = 'Airflow Test Email',
        html_content = 'Your Airflow Task has been successfully completed!',
    )