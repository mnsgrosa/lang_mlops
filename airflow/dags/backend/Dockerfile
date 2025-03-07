FROM langmlops/base-python:latest

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]