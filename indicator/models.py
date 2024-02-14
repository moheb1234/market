from django.db import models
from strategy.models import Strategy

class Indicator(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    open_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'open' , null= True)
    close_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'close' , null= True)



aggregated_settings = {
            'Moving Average Convergence Divergence (MACD)' : ['fast_period','slow_period','signal_period' ],
            'Relative Strength Index (RSI)' : ['upper_band' , 'lower_band' , 'ma_length' ],
            'Moving Average (MA)' : ['ma_type' , 'ma_size'] ,
            'Stochastic' : ['k_length' , 'k_smoothing' , 'd_smoothing']
        }

class Setting(models.Model):
    indicator = models.OneToOneField(to= Indicator , on_delete=models.CASCADE , related_name='settings' , null=True)
    time_frame = models.CharField(max_length=8)
    buy_sell = models.CharField(max_length=16)
    keep_signal = models.IntegerField()
    necessary = models.BooleanField()
    long_period = models.IntegerField(null=True)
    OHLCV_value = models.CharField(max_length=128 , null=True)
    short_period  = models.IntegerField(null=True)  
    consider = models.BooleanField(null=True) 
    fast_period = models.IntegerField(null=True)  #macd field
    slow_period = models.IntegerField(null=True)  #macd field
    signal_period = models.IntegerField(null=True) #macd field
    cross = models.CharField(max_length=256 , null=True) 
    upper_band = models.IntegerField(null= True)   # RSI field
    lower_band = models.IntegerField(null= True)   # RSI field
    ma_length = models.IntegerField(null= True)   # RSI ma field
    ma_type = models.CharField(max_length=32 , null=True) # ma field
    ma_size = models.IntegerField( null=True) # ma field
    k_length = models.IntegerField(null=True) # stoch field
    k_smoothing = models.IntegerField(null=True) # stoch field
    d_smoothing = models.IntegerField(null=True) # stoch field
    