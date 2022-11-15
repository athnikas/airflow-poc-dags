from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from random import randint

with DAG("my_dag", start_date=datetime(2021, 1, 1), schedule_interval=None, catchup=False) as dag:

    start = DummyOperator(task_id="start")

    extract = BashOperator(task_id="extract", bash_command="echo 'data extracted from source'")

    transform = BashOperator(task_id="transform", bash_command="echo 'data transformation applied'")

    load = BashOperator(task_id="load", bash_command="echo 'data loaded to target'")

    end = DummyOperator(task_id="end")

    start >> extract >> transform >> load >> end
