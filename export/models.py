from django.db import models
from bot.models import Bot


# get data from logic 
class Export(models.Model):
    bot = models.ForeignKey(to= Bot , on_delete= models.CASCADE)
    total_positions = models.IntegerField(null=True)
    long = models.IntegerField(null=True)
    short = models.IntegerField(null=True)
    liquidated = models.IntegerField(null=True)
    open = models.IntegerField(null=True)
    closed_by_take_profit = models.IntegerField(null=True)
    closed_by_stop_loss = models.IntegerField(null=True)
    closed_by_signal = models.IntegerField(null=True)
    total_profit = models.FloatField(null=True)
    total_loss = models.FloatField(null=True)
    turn_over = models.FloatField(null=True)
    order_amount = models.FloatField(null=True)
    leverage = models.IntegerField(null=True)
    take_profit = models.FloatField(null=True)
    stop_loss = models.FloatField(null=True)
    min_price_change = models.FloatField(null=True)
    max_price_change = models.FloatField(null=True)

class Asset_Position(models.Model):
    export = models.ForeignKey(Export , on_delete=models.CASCADE , related_name='asset_position_list')
    asset_name = models.CharField(max_length=50,null=True)
    position_side = models.CharField(max_length=10,null=True)
    open_time = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)
    entry_price = models.FloatField(null=True)
    qty = models.FloatField(null=True)
    closed_by = models.CharField(max_length=100)
    income = models.FloatField(null=True)
    total_profit = models.FloatField(null=True)
    total_loss = models.FloatField(null=True)
    turn_over = models.FloatField(null=True)

