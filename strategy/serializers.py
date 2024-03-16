from rest_framework import serializers
from .models import Strategy 
from indicator.serializers import IndicatorSerializer
from .managers import *
from bot.models import Bot
from django.core.exceptions import ObjectDoesNotExist



class StrategySerializer(serializers.ModelSerializer):
    open = IndicatorSerializer(many = True , allow_null= True , required=False )
    close = IndicatorSerializer(many = True , allow_null= True , required=False)
    class Meta:
        model = Strategy
        fields = ['id','name' , 'image' , 'description' , 'low_high_price' ,'min_price_allow' , 'max_price_allow' , 'min_sig_for_open' ,
        'min_sig_for_close' , 'user' , 'open' , 'close' ]
        read_only_fields = ['user']
    
    
    def create(self , validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return strategy_create(**validated_data)
        
    
    def update(self, instance , validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        pk = instance.id
        bots_name = []
        for bot in instance.bots.all():
            bots_name.append(bot.name)
        print(bots_name)
        instance.delete()
        validated_data['id'] = pk
        strategy = strategy_create(**validated_data)
        for name in bots_name:
            try:
                bot = Bot.objects.get(strategy=None , user= user, name= name)
                bot.strategy = strategy
                bot.save()
            except ObjectDoesNotExist:
                continue
        return strategy
        


class ShortStrategySerializer(serializers.ModelSerializer):  #summery of strategy data
        class Meta:
            model = Strategy
            fields = ['id','name' , 'image' , 'description']

