from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 6),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Snowflake connection parameters
SNOWFLAKE_CONN_ID = 'snowflake_default'
SNOWFLAKE_DATABASE = 'BI_PROJECT'
SNOWFLAKE_SCHEMA = 'PUBLIC'
SNOWFLAKE_TABLE = 'BI'

def prepare_data():
    # Read CSV file from the data folder
    df = pd.read_csv('/opt/airflow/data/stadiums_20241206_164848.csv')
    
    # Clean and prepare data if needed
    df = df.fillna('NULL')
    
    # Save as temporary CSV for Snowflake loading
    df.to_csv('/tmp/stadiums_cleaned.csv', index=False, header=True)

# Create DAG
dag = DAG(
    'stadiums_to_snowflake',
    default_args=default_args,
    description='Load stadiums data to Snowflake',
    schedule_interval=None,
    catchup=False
)

# Task 1: Data preparation
prepare_data_task = PythonOperator(
    task_id='prepare_data',
    python_callable=prepare_data,
    dag=dag
)

# Task 2: Create table in Snowflake
create_table = SnowflakeOperator(
    task_id='create_table',
    sql="""
    CREATE TABLE IF NOT EXISTS {}.{}.{} (
        stadium VARCHAR(255),
        capacity INTEGER,
        region VARCHAR(255),
        country VARCHAR(255),
        city VARCHAR(255),
        images VARCHAR(500),
        home_team VARCHAR(255),
        location VARCHAR(255)
    )
    """.format(SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_TABLE),
    snowflake_conn_id=SNOWFLAKE_CONN_ID,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    dag=dag
)

# Task 3: Load data into Snowflake
load_in_airflow = SnowflakeOperator(
    task_id='load_in_airflow',
    sql="""
    COPY INTO {}.{}.{}
    FROM @%stadiums_cleaned.csv
    FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1)
    ON_ERROR = CONTINUE
    """.format(SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_TABLE),
    snowflake_conn_id=SNOWFLAKE_CONN_ID,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    dag=dag
)

# Set task dependencies
prepare_data_task >> create_table >> load_in_airflow