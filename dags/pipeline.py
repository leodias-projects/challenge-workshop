from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG('pipeline', description='Master pipeline',
      schedule_interval="@daily",
      start_date=datetime(2022, 12, 31), catchup=False) as dag:
    
    start_pipeline = DummyOperator(task_id="start_pipeline")

    data_ingestion_trigger = TriggerDagRunOperator(task_id='data_ingestion_trigger',
                                                 trigger_dag_id='data_ingestion',
                                                 wait_for_completion=True)

    workshop_dag_trigger = TriggerDagRunOperator(task_id='challenge_dag_trigger',
                                                 trigger_dag_id='challenge_dag',
                                                 wait_for_completion=True)
                                                 
    #workshop_dag_sensor = ExternalTaskSensor(task_id='workshop_dag_sensor',
    #                                         external_dag_id ="workshop_dag")

    data_viz_trigger = TriggerDagRunOperator(task_id='data_viz_trigger',
                                             trigger_dag_id='data_viz',
                                             wait_for_completion=True)

    model_trigger = TriggerDagRunOperator(task_id='model_trigger',
                                          trigger_dag_id='model',
                                          wait_for_completion=True)

    end_of_pipeline = DummyOperator(task_id="end_of_pipeline")


start_pipeline >> data_ingestion_trigger >> workshop_dag_trigger

workshop_dag_trigger >> [data_viz_trigger, model_trigger]

[data_viz_trigger, model_trigger] >> end_of_pipeline