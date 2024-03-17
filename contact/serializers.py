from rest_framework import serializers
from .models import *
from rest_framework.exceptions import NotFound
from django.db import IntegrityError


class SignalPartnerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Signal
        fields = '__all__'
        read_only_fields = ['user' , 'object_type']
    
    def create(self , validated_data):
        object_type = self.context['view'].kwargs['type']
        user = self.context['request'].user
        if object_type == 'signal' or object_type == 'partner':
            validated_data['user'] = user
            validated_data['object_type'] = object_type
            try:
                return Signal.objects.create(**validated_data)
            except IntegrityError:
                raise serializers.ValidationError({'detail' : 'you can only create once'})
        raise NotFound({'detail' : 'url not found'})

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

    def create(self , validated_data):
        return Support.objects.create(**validated_data)


class HireRepresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = '__all__'
        read_only_fields = ['object_type']

    def create(self , validated_data):
        object_type = self.context['view'].kwargs['type']
        if object_type == 'hire' or object_type == 'represent':
            validated_data['object_type'] = object_type
            return Hire.objects.create(**validated_data)
        raise NotFound({'detail' : 'url not found'})