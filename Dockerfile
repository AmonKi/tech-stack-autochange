FROM python:3.7.0

RUN dbt run

EXPOSE 5000