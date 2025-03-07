from .backend.chroma import DBClient
from .pdfreader import Reader
from .frontend.APIClient import APIClient
from airflow import DAG
from datetime import datetime
from .frontend.schema import TextInput

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

my_reader = Reader()
client = APIClient()

def gather_pdfs():
    text_inputs = my_reader.workflow()
