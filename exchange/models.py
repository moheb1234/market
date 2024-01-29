from django.db import models
from users.models import Users

class Exchange(models.Model):
    user = models.ForeignKey(Users , on_delete= models.CASCADE)
    exchange_name = models.CharField(max_length=16)
    account_name = models.CharField(max_length=32)
    api_key = models.CharField(max_length=128, null=True)
    secret_key = models.CharField(max_length=128, null=True)
    max_allow_position = models.IntegerField()

    class Meta:
        unique_together = ('exchange_name' , 'account_name')
        