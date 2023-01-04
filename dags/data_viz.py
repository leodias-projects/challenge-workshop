from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from dependencies.data_viz import plot_fft, plot_statistics

with DAG('data_viz', description='Run stuff for learning',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1), catchup=False) as dag:
               
    start_visualization = DummyOperator(task_id='start_visualization')

    fft_viz = PythonOperator(task_id="fft_plot",
                            python_callable=plot_fft.main)

    statistics_viz = PythonOperator(task_id='statistic_plot',
                                    python_callable=plot_statistics.main)

    end_visualization = DummyOperator(task_id='end_visualization')
                        

start_visualization>> [fft_viz, statistics_viz] >> end_visualization