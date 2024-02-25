from rest_framework import serializers
from .models import *
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
        if value is not None:
            str_cross = json.dumps(value)
            return str_cross
        return ''

    def to_representation(self, instance):
        ret = super(MACDSerializer , self).to_representation(instance)
        indicator_name = instance.indicator.name
        if instance.cross == '':
            ret.pop('cross')
        else:
            ret['cross'] = json.loads(instance.cross)      
        return ret
    

class RSISerializer(serializers.ModelSerializer):
    class Meta:
        model = RSI
        exclude = ['indicator' , 'polymorphic_ctype' ]


class RSICrossSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSICross
        exclude = ['indicator' , 'polymorphic_ctype' ]


class RSIMaSerializer(serializers.ModelSerializer):
    cross = serializers.ListField()
    class Meta:
        model = RSIMa
        exclude = ['indicator' , 'polymorphic_ctype' ]
    
    def validate_cross(self, value):
        return json.dumps(value)
    
    def to_representation(self , instance ):
        ret = super(RSIMaSerializer , self).to_representation(instance)
        ret['cross'] = json.loads(instance.cross)
        return ret


class MASerializer(serializers.ModelSerializer):
    ma_sizes = serializers.ListField()
    class Meta:
        model = MA
        exclude = ['indicator' , 'polymorphic_ctype' ]
    
    def validate_ma_size(self , value):
        return json.dumps(value)

    def to_representation(self, instance):
        ret = super(MASerializer, self).to_representation(instance)
        ret['ma_sizes'] = json.loads(instance.ma_sizes)
        return ret


class OBVSerializer(serializers.ModelSerializer):
    cross = serializers.ListField(required=False)
    class Meta:
        model = OBV
        exclude = ['indicator' , 'polymorphic_ctype' ] 
    
    def validate_cross(self , value):
        if value is not None:
            return json.dumps(value)
        return ''

    def to_representation(self , instance):
        ret = super(OBVSerializer , self).to_representation(instance)
        if instance.cross == '':
            ret.pop('cross')
        else:
            ret['cross'] = json.loads(instance.cross)
        return ret


class STDSerializer(serializers.ModelSerializer):
    class Meta:
        model = STD
        exclude = ['indicator' , 'polymorphic_ctype' ]


class StochasticSerializer(serializers.ModelSerializer):
    for_buy_lower_upper = serializers.ListField()
    for_buy_lower = serializers.ListField()
    for_sell_lower_upper = serializers.ListField()
    for_sell_upper = serializers.ListField()

    class Meta:
        model = Stochastic
        exclude = ['indicator' , 'polymorphic_ctype' ]

    def validate_for_buy_lower_upper(self ,value):
        return json.dumps(value)
    
    def validate_for_buy_lower(self ,value):
        return json.dumps(value)

    def validate_for_sell_lower_upper(self ,value):
        return json.dumps(value)

    def validate_for_sell_upper(self ,value):
        return json.dumps(value)
    

    def to_representation(self , instance):
        ret = super(StochasticSerializer , self).to_representation(instance)
        ret['for_buy_lower_upper'] = json.loads(instance.for_buy_lower_upper)
        ret['for_buy_lower'] = json.loads(instance.for_buy_lower)
        ret['for_sell_lower_upper'] = json.loads(instance.for_sell_lower_upper)
        ret['for_sell_upper'] = json.loads(instance.for_sell_upper)
        return ret

class SettingPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'ind'
    model_serializer_mapping = {
        Setting : SettingSerializer ,
        MACD : MACDSerializer,
        RSI : RSISerializer,
        RSICross : RSICrossSerializer,
        RSIMa : RSIMaSerializer,
        MA : MASerializer,
        OBV : OBVSerializer,
        STD : STDSerializer,
        Stochastic : StochasticSerializer
    }


        

class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingPolymorphicSerializer()

    class Meta:
        model = Indicator
        fields = ['id' , 'name' , 'type' , 'settings']
    

    
