#!/usr/bin/env python
import os

from celery import Celery


CELERY_BROKER = os.getenv("CELERY_BROKER", "amqp://guest:guest@localhost:5672")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost")

app = Celery(
    "sample",
    broker=CELERY_BROKER,
    backend=CELERY_RESULT_BACKEND,
    include=["sample.tasks"],
)

if __name__ == "__main__":
    app.worker_main()
