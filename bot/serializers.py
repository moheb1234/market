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
        fields = ['id' ,'name' , 'user' ,'description' , 'image' , 'trade_market', 'order_type' , 'order_timeout'
         , 'spread' , 'classification' ,'leverage' , 'order_amount' , 'stop_loss' 
        ,'take_profit' , 'watchdog' , 'max_open_position_after_trend' , 'start_date' , 'end_date' ,
        'strategy' , 'market_accounts' , 'asset_name']
        read_only_fields = ['user']
        extra_kwargs = {
            'strategy': {'required' : True , 'allow_null' : False}
            }

    def required_dates(self ,data):
        try:
            if not 'start_date' in data.keys() or data['start_date'] == None:
                    raise serializers.ValidationError({'start_date' : 'this field can not be null'})
            if not 'end_date' in data.keys() or data['end_date'] == None:
                    raise serializers.ValidationError({'end_date' : 'this field can not be null'})
        except KeyError :
            pass

    def validate(self , data):
        try:
            bot_type = self.context['view'].kwargs['bot_type']
            if bot_type == 'back-test':
               self.required_dates(data)
            elif bot_type == 'trade':
                if 'start_date' in data.keys():
                    data['start_date'] = None
                if 'end_date' in data.keys():
                    data['end_date'] = None
                return data
            else :
                raise NotFound({'detail' : 'url address is wrong'})
        except KeyError : 
            pass
        return data

    def validate_trade_market(self , value):
        return json.dumps(value)
    
    def validate_spread(self , value):
        return json.dumps(value)
    
    def validate_classification(self , value):
        return json.dumps(value)
        
    
    def to_representation(self , instance):
        ret = super(BotSerializer , self).to_representation(instance)
        ret['trade_market'] = json.loads(instance.trade_market)
        if instance.spread == None:
            ret['spread'] = None
        else :
            ret['spread'] = json.loads(instance.spread)
        if instance.classification == None:
            ret['classification'] = None
        else :
            ret['classification'] = json.loads(instance.classification)
        try:
            if instance.bot_type == 'trade':
                ret.pop('start_date')    
                ret.pop('end_date')    
        except KeyError:
            pass
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
        bot_type = self.context['view'].kwargs['bot_type']
        user = self.context['request'].user
        validated_data['bot_type'] = bot_type
        validated_data['user'] = user
        bot = bot_create(**validated_data)
        # self.send_bot_data(bot)
        return bot
    
    def update(self , instance , validated_data):
        if instance.bot_type == 'back-test':
            self.required_dates(validated_data)
        pk = instance.id
        instance.delete()
        validated_data['id'] = pk
        validated_data['bot_type'] = instance.bot_type
        user = self.context['request'].user
        validated_data['user'] = user
        return bot_create(**validated_data)


class BotEventSerializer(serializers.Serializer):
    command = serializers.CharField(write_only=True)
    message = serializers.CharField(read_only=True)
    def update(self , instance , validated_data):
        command = validated_data['command']
        if command == 'start':
            pass
        elif command == 'stop':
            pass
        else:
            raise serializers.ValidationError({'detail' : 'command must be start or stop'})
        validated_data['message'] = 'The command was sent'
        return validated_data
    
        