from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import UserManager

class Users(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16 , null=True,unique=True)
    passport_number = models.CharField(max_length=32,null=True ,blank= True)
    card = models.CharField(max_length=200,null=True,blank= True)
    photo = models.CharField(max_length=200,null=True)
    birthday = models.DateField(null=True)
    country = models.CharField(max_length=16,null=True)
    city = models.CharField(max_length=16,null=True)
    secret_question = models.CharField(max_length=128,null=True)
    answer = models.CharField(max_length=128,null=True)
    verify_code = models.IntegerField(null=True)

