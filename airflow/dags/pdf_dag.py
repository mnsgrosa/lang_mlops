from backend.chroma import DBClient
from pdfreader import Reader
from frontend.APIClient import APIClient
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from frontend.schema import TextInput
import os


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

my_reader = Reader()
client = APIClient()

def gather_pdfs():
    try:
        my_reader.workflow()
    except:
        raise Exception('Error in gathering PDF files')
        return {'success':False}
    return {'success':True}

def upload_pdfs():
    try:
        client.post(my_reader.input_text)
    except:
        raise Exception(f"Error in uploading to API {os.listdir('/dags/pdf')}")
        return {'success': False}
    return {'success': True}

with DAG(
    'Upload_pdfs_to_api',
    default_args = default_args,
    description = 'A simple workflow for PDF processing and uploading',
    schedule_interval = timedelta(minutes = 5),
    catchup = False
) as dag:

    gathering_pdfs = PythonOperator(
        task_id = 'gather_pdfs',
        python_callable = gather_pdfs,
    )

    uploading_pdfs = PythonOperator(
        task_id = 'upload_pdfs',
        python_callable = upload_pdfs,
    )

    gathering_pdfs >> uploading_pdfs