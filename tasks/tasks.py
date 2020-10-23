from celery.decorators import task
from django.core.mail import send_mail
from .models import Task as ModelTask


@task
def task_expired(tasks_id):
    tasks = ModelTask.objects.get(id=tasks_id)
    email_list = []

    for users in tasks.team_member.values():
        email = users.get('email')
        email_list.append(email)

    subject = 'Task nr. {}'.format(tasks.id)
    message = 'Your task {} has been expired.'.format(tasks.title)
    mail_sent = send_mail(subject,
                          message,
                          'ulanbek.dt94@gmail.com',
                          email_list)
    return mail_sent
