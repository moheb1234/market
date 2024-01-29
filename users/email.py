from django.core.mail import send_mail
from django.conf import settings
def send_verify_code(email,verify_code):
    send_mail(subject= ' verify email' , message=f' verify code {verify_code} '
    ,from_email=settings.EMAIL_HOST_USER , recipient_list=[email] , fail_silently=False)