FROM python:3.6-slim

WORKDIR /app
RUN pip install https://github.com/celery/celery/archive/master.zip#egg=celery[redis,msgpack] numpy frozendict

COPY sample /app/sample

CMD python sample/app.py -Ofair -Q celery --loglevel=INFO
