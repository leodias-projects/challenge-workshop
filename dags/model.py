from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from dependencies.models import SVM_fft, SVM_statistics

with DAG('model', description='Run the machine learning model',
      schedule_interval=None,
      start_date=datetime(2022, 12, 31), catchup=False) as dag:
      
      start_model_run = DummyOperator(task_id="start_model_run")

      fft_model = PythonOperator(task_id="fft_model",
                                 python_callable=SVM_fft.main)

      statistics_model = PythonOperator(task_id="statistics_model",
                                 python_callable=SVM_statistics.main)

      end_model = DummyOperator(task_id="end_model")

start_model_run >> [fft_model, statistics_model] >> end_model
      
