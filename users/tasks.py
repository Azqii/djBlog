from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.contrib.auth.forms import PasswordResetForm

from .models import User


@shared_task
def send_reset_password_email(subject_template_name, email_template_name, context,
                              from_email, to_email, html_email_template_name):
    context['user'] = User.objects.get(pk=context['user'])
    PasswordResetForm().send_mail(
        subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name
    )
