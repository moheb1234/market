from django.db import models
from strategy.models import Strategy 
from exchange.models import Exchange


class Bot(models.Model):
    market_accounts = models.ManyToManyField(to= Exchange)
    strategy = models.ForeignKey(to= Strategy , on_delete= models.CASCADE )
    bot_type = models.CharField(max_length=16)
    name = models.CharField(max_length=100 , blank=False)
    description = models.TextField(null=True)
    image = models.TextField()
    trade_market = models.CharField(max_length=255)
    order_type = models.CharField(max_length=32 , null= True)
    order_timeout = models.CharField(max_length=64)
    spread = models.CharField(max_length=255 , null= True)
    classification = models.CharField(max_length=255 , null= True)
    order_amount = models.FloatField(null= True  ,default=30)
    leverage = models.FloatField(null= True , default= 20)
    stop_loss = models.FloatField()
    take_profit = models.FloatField(null= True , default= 5)
    watchdog = models.FloatField(null= True , default= 5)
    max_open_position_after_trend = models.FloatField()
    start_date = models.CharField(max_length= 64 ,null=True)
    end_date = models.CharField(max_length= 64,null=True) 


class Asset(models.Model):
    name = models.CharField(max_length=200, blank=False)
    trade_market = models.CharField(max_length=32)
    classification = models.IntegerField()
    leverage = models.IntegerField()
    order_amount = models.FloatField()
    bot = models.ForeignKey(Bot , on_delete=models.CASCADE , related_name='asset_name' , null= True)
