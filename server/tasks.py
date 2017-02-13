# -*- coding: utf-8 -*-


from celery import Celery
from backend.configuration import Configuration


celery = Celery(Configuration.NAME, broker=Configuration.REDIS_URI)
celery.conf.update(
    BROKER_URL=Configuration.REDIS_URI,
    CELERY_RESULT_BACKEND=Configuration.REDIS_URI
)


@celery.task
def dummy():
    pass
