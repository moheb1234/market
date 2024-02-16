from rest_framework import serializers
from .models import Setting , Indicator
from .models import aggregated_settings
import json


class SettingSerializer(serializers.ModelSerializer):
    cross = serializers.ListField()
    class Meta:
        model = Setting
        exclude = ['indicator']

    
    def validate_cross(self , value):
        str_cross = ','.join(map(str,value))
        return str_cross

    
    def pop_unused_field(self , keep_indicator ,ret):
        for indicator , fields in aggregated_settings.items():
                if indicator == keep_indicator:
                    continue
                else:
                    for field in fields:
                        ret.pop(field)
    
    def to_representation(self, instance):
        ret = super(SettingSerializer , self).to_representation(instance)
        indicator_name = instance.indicator.name
        if indicator_name.startswith('Relative Strength Index'):
            indicator_name = 'Relative Strength Index (RSI)'
        if indicator_name in aggregated_settings.keys():
            self.pop_unused_field(indicator_name , ret)
        ret['cross'] = json.loads(f'[{instance.cross}]')        
        return ret
        

class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingSerializer()

    class Meta:
        model = Indicator
        fields = ['id' , 'name' , 'type' , 'settings']
    
    
