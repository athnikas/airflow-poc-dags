from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import logging
import sys

# Set Task Logger to INFO for better task logs
log = logging.getLogger("airflow.task")
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
log.addHandler(handler)

with DAG("dbt_dag", start_date=datetime(2021, 1, 1), schedule_interval=None, catchup=False) as dag:

    start = DummyOperator(task_id="start")

    dbt_model = BashOperator(
        task_id="dbt_model", bash_command="cd /opt/postgres_dbt && dbt run --select hosts_s --profiles-dir ."
    )

    end = DummyOperator(task_id="end")

    start >> dbt_model >> end
