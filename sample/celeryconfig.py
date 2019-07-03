import os

broker_url = os.getenv("CELERY_BROKER", "amqp://guest:guest@localhost:5672")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost")
imports = ("sample.tasks",)
task_serializer = "msgpack"
result_serializer = "msgpack"
accept_content = ("json", "msgpack")
