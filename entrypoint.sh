airflow db migrate

# Create user if not exists
if ! airflow users list | grep -q $AIRFLOW_USER; then
    airflow users create \
        --username $AIRFLOW_USER\
        --firstname $AIRFLOW_FIRSTNAME \
        --lastname $AIRFLOW_LASTNAME\
        --role $AIRFLOW_ROLE \
        --email $AIRFLOW_EMAIL \
        --password $AIRFLOW_PASSWORD
fi

airflow webserver