from django.db import models
from django.contrib.auth.models import AbstractUser 


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    verify_code = models.IntegerField(null=True)
    referral_code = models.IntegerField(null=True)

class Profile(models.Model):
    user = models.OneToOneField(to= Users , on_delete= models.CASCADE)
    phone_number = models.CharField(max_length=16 , null=True,unique=True)
    passport_number = models.ImageField(upload_to = 'passport_number',null=True)
    self_photo = models.ImageField(upload_to = 'self_photo',null=True)
    birthday = models.DateField(null=True)
    country = models.CharField(max_length=32,null=True)
    city = models.CharField(max_length=32,null=True)
    secret_question = models.TextField(null=True)
    answer = models.TextField(null=True)







