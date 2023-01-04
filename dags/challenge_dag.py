from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.filesystem import FileSensor
from dependencies.preprocessing import download_data, creation_statistics, creation_fft

with DAG('challenge_dag', description='Run stuff for learning',
      schedule_interval=None,
      start_date=datetime(2022, 12, 31), catchup=False) as dag:
          
          
      dummy = DummyOperator(task_id='good_luck')
                            
      end_creation_of_files = DummyOperator(dag=dag,
                                          task_id='finished_creation_of_files') 


sensor_data_upload >> end_creation_of_files
