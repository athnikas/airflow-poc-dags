from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG("dbt_dag", start_date=datetime(2021, 1, 1), schedule_interval=None, catchup=False) as dag:

    start = DummyOperator(task_id="start")

    dbt_model = BashOperator(
        task_id="dbt_model", bash_command="cd /opt/postgres_dbt && dbt run --select hosts_s --profiles dir ."
    )

    end = DummyOperator(task_id="end")

    start >> dbt_model >> end
