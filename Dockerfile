FROM python:3.6-slim

WORKDIR /app
RUN pip install celery[redis] numpy frozendict

COPY sample /app/sample

CMD python sample/app.py -Ofair -Q celery --loglevel=INFO
