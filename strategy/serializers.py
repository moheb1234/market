from rest_framework import serializers
from .models import Strategy 
from indicator.serializers import IndicatorSerializer
from .managers import *



class StrategySerializer(serializers.ModelSerializer):
    open = IndicatorSerializer(many = True , allow_null= True , required=False )
    close = IndicatorSerializer(many = True , allow_null= True , required=False)
    class Meta:
        model = Strategy
        fields = ['id','name' , 'image' , 'description' , 'min_price_allow' , 'max_price_allow' , 'min_sig_for_open' ,
        'min_sig_for_close' , 'user' , 'open' , 'close' ]
        read_only_fields = ['user']
    
    
    def create(self , validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return strategy_create(**validated_data)
        
    
    def update(self, instance , validated_data):
        pk = instance.id
        instance.delete()
        validated_data['id'] = pk
        return self.create(validated_data)
        


class ShortStrategySerializer(serializers.ModelSerializer):  #summery of strategy data
        class Meta:
            model = Strategy
            fields = ['id','name' , 'image' , 'description']

