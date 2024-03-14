from django.db import models
from users.models import Users

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

    class Meta:
        unique_together = ('user' , 'object_type')

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

