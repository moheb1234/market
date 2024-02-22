from django.db import models
from users.models import Users

class Strategy(models.Model):
    user = models.ForeignKey(to= Users , on_delete= models.CASCADE )
    name = models.CharField(max_length=200 , blank=False)
    image = models.CharField(max_length=400)
    description = models.CharField(max_length=400, null = True)
    min_price_allow = models.FloatField(default=0)
    max_price_allow = models.FloatField(default=0)
    min_sig_for_open = models.IntegerField(default=0)
    min_sig_for_close = models.IntegerField(null=True , default=0)
    low_high_price = models.IntegerField(default=5)

    class Meta:
        unique_together = ('user','name')



        


