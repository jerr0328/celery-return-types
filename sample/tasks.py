import numpy as np
from celery.utils.log import get_task_logger
from frozendict import frozendict

from .app import app

logger = get_task_logger(__name__)


@app.task
def do_work():
    """Example returning some weird types"""
    return {
        "normal": "string",
        "numpy": [np.float32(3.5), np.int_(6), np.float_(3.14)],
        "frozen": frozendict({"sample": "value"}),
    }
