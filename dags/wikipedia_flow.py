from datetime import datetime, timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from pipelines.wikipedia import (
    get_wikipedia_page,
    extract_stadium_data,
    transform_wikipedia_data
)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_stadium_data_task():
    url = "htt  ps://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"
    html_content = get_wikipedia_page(url)
    data = extract_stadium_data(html_content)
    return data

def transform_stadium_data_task(ti):
    stadiums_data = ti.xcom_pull(task_ids='extract_data')
    if not stadiums_data:
        raise ValueError("No data received from extraction task")
    transformed_df = transform_wikipedia_data(stadiums_data)
    return transformed_df.to_dict(orient='records')

def load_stadium_data_task(ti):
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    if not transformed_data:
        raise ValueError("No data received from transform task")
    df = pd.DataFrame(transformed_data)
    
    # Save to CSV with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    df.to_csv(f'/opt/airflow/data/stadiums_{timestamp}.csv', index=False)

with DAG(
    'wikipedia_stadiums_etl',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 12, 7),
    catchup=False
) as dag:

    extract_data = PythonOperator(
        task_id='extract_data',
        python_callable=extract_stadium_data_task,
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=transform_stadium_data_task,
    )

    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_stadium_data_task,
    )

    extract_data >> transform_data >> load_data