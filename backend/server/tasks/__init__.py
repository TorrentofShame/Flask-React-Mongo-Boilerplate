# -*- coding: utf-8 -*-
"""
    server.tasks.__init__
    ~~~~~~~~~~~~~~~~~~~~~

"""
from celery import Celery

def make_celery(app):
    """Initialize the Celery Application"""
    
    celery = Celery(__name__,
                    broker=app.config["CELERY_BROKER_URL"],
                    include=["server.tasks.mail_tasks"],
                    backend=app.config["CELERY_RESULT_BACKEND"]
                    )
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

