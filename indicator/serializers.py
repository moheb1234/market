from rest_framework import serializers
from .models import Setting , Indicator ,MACD
from .models import aggregated_settings
from rest_polymorphic.serializers import PolymorphicSerializer
import json


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        exclude = ['indicator' , 'polymorphic_ctype' ]

    

class MACDSerializer(serializers.ModelSerializer):
    cross = serializers.ListField(required=False)
    class Meta :
        model = MACD
        exclude = ['indicator' , 'polymorphic_ctype' ]

    def validate_cross(self , value):
        if value:
            str_cross = ','.join(value)
            return str_cross
        if len(value) == 0 :
            return 'empty'
        return ''

    def to_representation(self, instance):
        ret = super(MACDSerializer , self).to_representation(instance)
        indicator_name = instance.indicator.name
        
        if instance.cross == '':
            ret.pop('cross')
        elif instance.cross == 'empty':
            ret['cross'] = []
        else:
            ret['cross'] = instance.cross.split(',')       
        return ret

class SettingPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'ind'
    model_serializer_mapping = {
        Setting : SettingSerializer ,
        MACD : MACDSerializer
    }


        

class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingPolymorphicSerializer()

    class Meta:
        model = Indicator
        fields = ['id' , 'name' , 'type' , 'settings']
    
    
