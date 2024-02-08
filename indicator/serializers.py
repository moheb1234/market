from rest_framework import serializers
from .models import Setting , Indicator
from .models import aggregated_settings


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        exclude = ['indicator']

    
    def pop_unused_field(self , name ,ret):
        for indicator , fields in aggregated_settings.items():
                if indicator == name:
                    continue
                else:
                    for field in fields:
                        ret.pop(field)
    
    def to_representation(self, instance):
        ret = super(SettingSerializer , self).to_representation(instance)
        if instance.indicator.name == 'RSI':
            self.pop_unused_field('RSI' , ret)
        
        elif instance.indicator.name == 'MACD':
            self.pop_unused_field('MACD', ret)
        
        elif instance.indicator.name == 'Ma':
            self.pop_unused_field('MA' , ret)

        elif instance.indicator.name == 'STOCH':
            self.pop_unused_field('STOCH' , ret)
        
        return ret
        

class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingSerializer()

    class Meta:
        model = Indicator
        fields = ['id' , 'name' , 'type' , 'settings']
    
    
