#!/usr/bin/env python
from celery import Celery


app = Celery("sample")
app.config_from_object("sample.celeryconfig")

if __name__ == "__main__":
    app.worker_main()
