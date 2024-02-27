from django.db import models
from strategy.models import Strategy
from polymorphic.models import PolymorphicModel

class Indicator(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    open_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'open' , null= True)
    close_str = models.ForeignKey(Strategy , on_delete= models.CASCADE , related_name= 'close' , null= True)


class Setting(PolymorphicModel):
    indicator = models.OneToOneField(to= Indicator , on_delete=models.CASCADE , related_name='settings' , null=True)
    time_frame = models.CharField(max_length=8 , default='4h')
    buy_sell = models.CharField(max_length=16 , default= ' both')
    keep_signal = models.CharField(max_length=16 ,default='0')
    necessary = models.BooleanField(default= True)
 

class MACD(Setting):
    ohlcv_value = models.CharField(max_length=128 , default= 'close')
    fast_length = models.IntegerField(default=12)  
    slow_length = models.IntegerField(default = 26)  
    signal_smoothing  = models.IntegerField(default=9) 
    cross = models.CharField(max_length= 128 , default='' , null= True)
    consider = models.BooleanField(default=False , null= True) 

class RSI(Setting):
    ohlcv_value   = models.CharField(max_length=16 , default= 'close')
    rsi_length  = models.IntegerField(default=14)
    signal_upper_band =  models.IntegerField(default=70)
    signal_lower_band = models.IntegerField(default=30)

class RSICross(Setting):
    ohlcv_value   = models.CharField(max_length=16 , default= 'close')
    rsi_length  = models.IntegerField(default=14)
    signal_upper_greater =  models.IntegerField(default=70)
    signal_lower_less = models.IntegerField(default=30)

class RSIMa(Setting):
    ohlcv_value   = models.CharField(max_length=16 , default= 'close')
    rsi_length  = models.IntegerField(default=14)
    signal_upper_band =  models.IntegerField(default=70)
    signal_lower_band = models.IntegerField(default=30)
    ma_type = models.CharField(max_length=32 , default='EMA')
    ma_length = models.IntegerField(default=14)
    cross = models.CharField(max_length=128) 
    consider = models.BooleanField(default=False)

class MA(Setting):
    ohlcv_value   = models.CharField(max_length=16 , default= 'close')
    ma_type = models.CharField(max_length=32 , default='EMA')
    ma_sizes = models.CharField(max_length=128)
    


class OBV(Setting):
    ma_type_obv = models.CharField(max_length=32 , default='EMA')
    length = models.IntegerField(default=5)
    cross_with_zero = models.BooleanField(default=True)
    ma_type = models.CharField(max_length=32 , default='EMA' , null= True)
    ma_length = models.IntegerField(default=14 , null= True)
    cross = models.CharField(max_length=128 , null= True)
    consider = models.BooleanField(default=False , null= True)


class STD(Setting):
    ohlcv_value   = models.CharField(max_length=16 , default= 'close')
    length = models.IntegerField(default=20)
    callback =models.IntegerField(default=100)
    price_percent = models.IntegerField(default=60)
    ma_type = models.CharField(max_length=32 , default= 'EMA' , null= True)
    ma_length  = models.IntegerField(default=14 , null= True)


class Stochastic(Setting):
    k_length  = models.IntegerField(default=14)
    k_smooth  = models.IntegerField(default=3)
    d_smooth = models.IntegerField(default=7)
    signal_upper_band = models.IntegerField(default=80)
    signal_lower_band = models.IntegerField(default=20)
    consider = models.BooleanField(default=False)
    cross_k_d = models.BooleanField(default=False)
    for_buy_lower_upper  = models.CharField(max_length=128, default='' , null= True)
    for_buy_lower  = models.CharField(max_length=128 , default='' , null= True)
    for_sell_lower_upper  = models.CharField(max_length=128 , default='' , null= True)
    for_sell_upper  = models.CharField(max_length=128 , default='' , null= True)



    


            