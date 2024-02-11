from django.db import models
from strategy.models import Strategy 
from exchange.models import Exchange
class Asset(models.Model):
    name = models.CharField(max_length=200, blank=False)


class Bot(models.Model):
    exchange = models.ForeignKey(to= Exchange ,on_delete= models.CASCADE)
    strategy = models.ForeignKey(to= Strategy , on_delete= models.CASCADE )
    name = models.CharField(max_length=100 , blank=False)
    trade_market = models.CharField(max_length=32 , null=True)
    leverage = models.FloatField()
    order_amount = models.FloatField()
    stop_loss = models.FloatField()
    take_profit = models.FloatField()
    watch_dog = models.FloatField(null= True)
    trade_now = models.BooleanField()
    is_in_process = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    asset_list_names = models.ManyToManyField(to= Asset)   
