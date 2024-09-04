from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_registration_email(user_email):
    subject = "Welcome to Our Website!"
    plain_message = "Registered Successfully"
    from_email = "stcoleridge88@gmail.com"
    to_email = user_email
    send_mail(subject, plain_message, from_email, [to_email])
