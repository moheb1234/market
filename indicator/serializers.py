from rest_framework import serializers
from .models import Setting , Indicator
from collections import OrderedDict


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        exclude = ['indicator']
    
    def to_representation(self, instance):
        result = super(SettingSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    
    


class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingSerializer()

    class Meta:
        model = Indicator
        fields = ['id' , 'name' , 'type' , 'settings']
    
