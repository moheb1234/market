from rest_framework import serializers
from.models import Bot , Asset
from users.exceptions import Server_Error
from strategy.serializers import StrategySerializer
from exchange.serializer import ExchangeSerializer
from django.forms.models import model_to_dict
from .managers import bot_create
import requests
import json


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__' 


class BotSerializer(serializers.ModelSerializer):
    strategy = StrategySerializer(read_only=True)
    exchange = ExchangeSerializer(read_only=True)
    asset_list_names = AssetSerializer(many = True , allow_null=True , required=False)
    

    class Meta:
        model = Bot
        fields = ['id' ,'name' , 'leverage' , 'order_amount' , 'stop_loss' ,'take_profit' , 'watch_dog' , 'trade_now' 
        , 'start_date' , 'end_date' ,'strategy' , 'exchange' , 'asset_list_names']
    
    # send bot data to indicator 
    def send_bot_data(self,bot):
        url = 'http://127.0.0.1:8001/indicator/data/'
        data = json.dumps(BotSerializer(instance=bot).data)
        response =  requests.post(url=url ,data = {'data':data})
        if response.status_code!=201:
            bot.delete()
            raise Server_Error()
 
    def create(self , validated_data):
        strategy_id = self.context['view'].kwargs['str_id']
        exchange_id = self.context['view'].kwargs['ex_id']
        bot = bot_create(strategy_id , exchange_id , **validated_data)
        # self.send_bot_data(bot)
        return bot
        