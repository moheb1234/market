from django.db import models
from strategy.models import Strategy


class Setting(models.Model):
    long_period = models.IntegerField(null=True)
    consider = models.BooleanField(null=True)
    OHLCV_value = models.CharField(max_length=128 , null=True)
    short_period  = models.IntegerField(null=True)  
    fast_period = models.IntegerField(null=True)  #macd field
    slow_period = models.IntegerField(null=True)  #macd field
    signal_period = models.IntegerField(null=True) #macd field
    cross = models.CharField(max_length=256 , null=True) #macd field
    upper_band = models.IntegerField(null= True)   # RSI field
    lower_band = models.IntegerField(null= True)   # RSI field
    rsi_length = models.IntegerField(null= True)   # RSI field
    rsi_type = models.CharField( max_length=32, null= True)   # RSI field




class Indicator(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    settings = models.ForeignKey(Setting , on_delete=models.CASCADE,null=True)
    open_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'open' , null= True)
    close_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'close' , null= True)
    time_frame = models.CharField(max_length=8)
    buy_sell = models.CharField(max_length=16)
    keep_signal = models.IntegerField()
    necessary = models.BooleanField()
    