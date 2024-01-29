from rest_framework import serializers
from .models import Exchange
from users.serializers import UserRegisterSerializer

class ExchangeSerializer(serializers.ModelSerializer):
    user  = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Exchange
        fields = '__all__'
        
    def create(self , validated_data):
        user =  self.context['request'].user
        validated_data['user'] = user
        return Exchange.objects.create(**validated_data)
    
