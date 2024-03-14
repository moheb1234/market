from rest_framework import serializers
from .models import *


class SignalSerializer(serializers.ModelSerializer):
    class Meta :
        model = Signal
        exclude = ['object_type']

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

    def create(self , validated_data):
        return Support.objects.create(**validated_data)


class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        exclude = ['object_type']

    def create(self , validated_data):
        return Hire.objects.create(**validated_data)