from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator

with DAG('data_ingestion', 
         description='Upload data to AWS S3 bucket',
         schedule_interval=None,
         start_date=datetime(2022, 12, 31), 
         catchup=False) as dag:
    
    start_data_ingestion = DummyOperator(task_id="start_data_ingestion")
    
    message = "Pretend that there is an actual ingestion here xD...have fun in the workshop! The prize will be     hmmm little smart !! "
    data_ingestion = BashOperator(task_id="s3_data_ingestion",
                                bash_command=f"echo {message} | sleep 10s")
    
    end_data_ingestion = DummyOperator(task_id="end_data_ingestion")


start_data_ingestion >> data_ingestion >> end_data_ingestion

