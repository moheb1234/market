from rest_framework import serializers
from .models import Strategy 
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from indicator.serializers import IndicatorSerializer
from indicator.models import Indicator , Setting
from .managers import *
from drf_writable_nested import WritableNestedModelSerializer



class StrategySerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    open = IndicatorSerializer(many = True , allow_null= True , required=False )
    close = IndicatorSerializer(many = True , allow_null= True , required=False)
    class Meta:
        model = Strategy
        fields = '__all__'
        read_only_fields = ['user']
    
    def create(self , validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return strategy_create(**validated_data)
    
    def update(self, instance , validated_data):
        instance.delete()
        return self.create(validated_data)
        


class ShortStrategySerializer(serializers.ModelSerializer):  #summery of strategy data
        class Meta:
            model = Strategy
            fields = ['id','name' , 'image' , 'description']

