from celery import shared_task
from django.core.mail import send_mail

@shared_task
def my_periodic_task():
    # Your periodic logic here
    send_mail(
        "Test email for Karma",
        "Here is the message.",
        "vikassrinitb@gmail.com",
        ["vikassrinitb@gmail.com"],
        fail_silently=False,
    )
