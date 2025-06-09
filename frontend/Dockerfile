FROM langmlops/base-python:latest

WORKDIR /app

COPY frontend/. /app

COPY schemas /app/schemas

EXPOSE 8501

CMD ["streamlit", "run", "st.py"]