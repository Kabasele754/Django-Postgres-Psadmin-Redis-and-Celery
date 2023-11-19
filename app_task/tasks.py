from celery import shared_task
from time import sleep
import json
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Task


@shared_task
def sub(x, y):
    sleep(10)
    return x - y

#  send mail

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    

@shared_task
def send_task_reminder_emails():
    current_time = timezone.now()
    expired_tasks = Task.objects.filter(due_date__lt=current_time)
    
    for task in expired_tasks:
        subject = 'Rappel : Tâche expirée'
        message = f'La tâche "{task.title}" est expirée. Veuillez la compléter dès que possible.'
        send_mail(subject, message, settings.EMAIL_HOST_USER,  [task.user.email])

    ongoing_tasks = Task.objects.filter(due_date__gte=current_time)
    
    for task in ongoing_tasks:
        subject = 'Rappel : Tâche en cours'
        message = f'La tâche "{task.title}" est toujours en cours. Assurez-vous de la terminer à temps.'
        send_mail(subject, message, settings.EMAIL_HOST_USER,  [task.user.email])

