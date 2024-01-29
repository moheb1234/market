from rest_framework import serializers
from .models import Setting , Indicator


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class IndicatorSerializer(serializers.ModelSerializer):
    settings = SettingSerializer()

    class Meta:
        model = Indicator
        exclude = ['open_str' , 'close_str']
    