from django.core.mail import send_mail
from email.utils import formataddr
from django.conf import settings
def send_verify_code(email,verify_code , username):
    from_emil = formataddr(('Market' ,settings.EMAIL_HOST_USER))
    send_mail(subject= ' verify email' , message=f'welcome dear {username} \n verify code : {verify_code} '
    ,from_email=from_emil , recipient_list=[email] , fail_silently=False)