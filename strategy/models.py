from django.db import models
from users.models import Users

class Strategy(models.Model):
    user = models.ForeignKey(to= Users , on_delete= models.CASCADE )
    name = models.CharField(max_length=200 , blank=False , null=False )
    image = models.CharField(max_length=400)
    description = models.CharField(max_length=400, null = True)
    min_price_allow = models.FloatField(null=True)
    max_price_allow = models.FloatField(null=True)
    min_sig_for_open = models.IntegerField()
    min_sig_for_close = models.IntegerField(null=True)

    class Meta:
        unique_together = ('user','name')



        


