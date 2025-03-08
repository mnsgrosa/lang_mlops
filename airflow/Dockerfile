FROM langmlops/base-python:latest

ARG AIRFLOW_VERSION=2.7.1

RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.11.txt"

RUN mkdir -p ${AIRFLOW_HOME}/dags
RUN mkdir -p ${AIRFLOW_HOME}/logs
RUN mkdir -p ${AIRFLOW_HOME}/plugins
RUN mkdir -p ${AIRFLOW_HOME}/config

COPY dags/ ${AIRFLOW_HOME}/dags/
COPY plugins/ ${AIRFLOW_HOME}/plugins/
COPY config/ ${AIRFLOW_HOME}/config/

RUN airflow db init

EXPOSE 8080

CMD ['airflow', 'webserver']