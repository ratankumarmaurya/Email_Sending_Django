from django.conf import settings
from django.core.mail import send_mail

def send_email_client():
    subject="Django Email"
    message="Hello how are you "
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['rstarx42@gmail.com','mauryaratan42@gmail.com']
    send_mail(subject,message, from_email, recipient_list)
