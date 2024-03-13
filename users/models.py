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

class Signal(models.Model):
    user = models.OneToOneField(to= Users , on_delete= models.CASCADE)
    object_type = models.CharField(max_length=16 , default='signal') # or partner with us
    telegram_id = models.CharField(max_length=32)
    time_for_signal = models.CharField(max_length=128)
    favorite_asset_names = models.TextField()
    exchange_names = models.TextField()
    favorite_time_frames = models.TextField()
    rules = models.TextField()
    wallet_amount = models.FloatField()

class Support(models.Model):
    name = models.CharField(max_length=16 , unique=True)
    email = models.EmailField(unique= True)
    message = models.TextField()

class Hire(models.Model):
    object_type = models.CharField(max_length=16  , default = 'hire')  # or represent us
    name = models.CharField(max_length=64 , unique=True)
    email = models.EmailField(unique= True)
    job_title = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    cv = models.FileField(upload_to='cv' )
    descriptions = models.TextField()
    passport_number = models.ImageField(upload_to = 'passport_number')
    self_photo = models.ImageField(upload_to = 'self_photo')





