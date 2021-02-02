# -*- coding: utf-8 -*-
"""
    server.tasks.mail_tasks
    ~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask_mail import Message
from server import celery, mail


@celery.task
def send_async_email(subject, recipient, text_body, html_body):
    """Sends an Email"""
    msg = Message(subject=subject, recipients=[recipient])
    msg.body = text_body
    msg.html = html_body

