# -*- coding: utf-8 -*-
"""
    server.common.mail
    ~~~~~~~~~~~~~~~~~~

"""
from flask import render_template, request, url_for
from server.tasks.mail_tasks import send_async_email


def send_password_recovery_email(user, token):
    """Sends a password recovery email to the user"""
    href = f"{request.base_url}/{token}"
    send_async_email.delay(subject=f"Knight Hacks Password Recovery. {user.username}",
                           recipient=user.email,
                           text_body=render_template("emails/password_recovery.txt", user=user),
                           html_body=render_template("emails/password_recovery.html", user=user, href=href))


def send_registration_email(user, token):
    """Sends an registration verification email to the user"""
    href = f"{request.base_url}/verifyemail/{token}"
    send_async_email.delay(subject=f"Knight Hacks Password Recovery. {user.username}",
                           recipient=user.email,
                           text_body=render_template("emails/registration.txt", user=user),
                           html_body=render_template("emails/registration.html", user=user, href=href))



def send_acceptance_email(user, token):
    """Sends an acceptance email to the user"""
    href = f"{request.base_url}/{token}"
    send_async_email.delay(subject=f"Knight Hacks Password Recovery. {user.username}",
                           recipient=user.email,
                           text_body=render_template("emails/acceptance.txt", user=user),
                           html_body=render_template("emails/acceptance.html", user=user, href=href))


