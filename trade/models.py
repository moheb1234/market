from django.db import models
from bot.models import Bot

class Order(models.Model):
    bot = models.ForeignKey(Bot , on_delete= models.CASCADE)
    asset_name = models.CharField(max_length=32)
    position_side = models.CharField(max_length=32)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    entry_price = models.FloatField()
    qty = models.FloatField()
    closed_by = models.CharField(max_length= 16)
    income = models.FloatField()
    profit = models.FloatField()
    loss = models.FloatField()
    turnover = models.FloatField()



