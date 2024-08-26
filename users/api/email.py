from django.core.mail import send_mail


class EmailService:
    def send_registration_email(self, user):
        subject = "Welcome to Our Website!"
        plain_message = "Registered Successfully"
        from_email = 'stcoleridge88@gmail.com'
        to_email = user.email
        send_mail(subject, plain_message, from_email, [to_email])