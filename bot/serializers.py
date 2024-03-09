from rest_framework import serializers
from.models import Bot , Asset
from users.exceptions import Server_Error
from strategy.serializers import StrategySerializer
from exchange.serializer import ExchangeSerializer
from .managers import bot_create
import requests
import json
from rest_framework.exceptions import NotFound


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        exclude = ['bot']  


class BotSerializer(serializers.ModelSerializer):
    asset_name = AssetSerializer(many = True , allow_null=True , required=False)
    trade_market = serializers.ListField()
    spread = serializers.ListField(required=False)
    classification = serializers.ListField(required = False)
    class Meta:
        model = Bot
        fields = ['id' ,'name' , 'description' , 'image' , 'trade_market', 'order_type' , 'order_timeout'
         , 'spread' , 'classification' ,'leverage' , 'order_amount' , 'stop_loss' 
        ,'take_profit' , 'watch_dog' , 'max_open_position_after_trend' , 'start_date' , 'end_date' ,
        'strategy' , 'market_accounts' , 'asset_name']

    def validate(self , data):
        bot_type = self.context['view'].kwargs['bot_type']
        if bot_type == 'back-test':
            if not 'start_date' in data.keys():
                raise serializers.ValidationError({'start_date' : 'this field is required'})
            if not 'end_date' in data.keys():
                raise serializers.ValidationError({'end_date' : 'this field is required'})
        elif bot_type == 'trade':
            return data
        else :
            raise NotFound({'detail' : 'url address is wrong'})

            
        return data

    def validate_trade_market(self , value):
        return json.dumps(value)
    
    def validate_spread(self , value):
        return json.dumps(value)
    
    def validate_classification(self , value):
        return json.dumps(value)
        
    
    def to_representation(self , instance):
        ret = super(BotSerializer , self).to_representation(instance)
        ret['strategy'] = StrategySerializer(instance= instance.strategy).data
        ret['market_accounts'] = ExchangeSerializer(instance= instance.market_accounts , many = True).data
        ret['trade_market'] = json.loads(instance.trade_market)
        if instance.spread == None:
            ret['spread'] = None
        else :
            ret['spread'] = json.loads(instance.spread)
        if instance.classification == None:
            ret['classification'] = None
        else :
            ret['classification'] = json.loads(instance.classification)
        bot_type = self.context['view'].kwargs['bot_type']
        if bot_type == 'trade':
            if 'start_date' in ret.keys():
                ret.pop('start_date')
            if 'end_date' in ret.keys():
                ret.pop('end_date') 
        return ret

    # send bot data to indicator 
    def send_bot_data(self,bot):
        url = 'http://127.0.0.1:8001/indicator/data/'
        data = json.dumps(BotSerializer(instance=bot).data)
        response =  requests.post(url=url ,data = {'data':data})
        if response.status_code!=201:
            bot.delete()
            raise Server_Error()
 
    def create(self , validated_data):
        bot = bot_create(**validated_data)
        # self.send_bot_data(bot)
        return bot
        