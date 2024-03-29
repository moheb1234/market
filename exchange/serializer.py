from rest_framework import serializers
from .models import Exchange
from users.serializers import UserRegisterSerializer
import socket

class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        exclude = ['user'] 
        
    def create(self , validated_data):
        user =  self.context['request'].user
        validated_data['user'] = user
        is_exist = Exchange.objects.filter(user= user , account_name=validated_data['account_name'] # check account name and exchange name unique together
        , exchange_name= validated_data['exchange_name']).exists()
        if is_exist:
            raise serializers.ValidationError({'detail':'account name and exchange name must be unique together'})
        return Exchange.objects.create(**validated_data)
    

class ExchangeBulkSaveSerializer(serializers.Serializer):
    exchanges =  ExchangeSerializer(many = True)

    def delete(self):
        user =  self.context['request'].user
        user_exchanges = Exchange.objects.filter(user=user)
        for ex in user_exchanges:
            ex.delete()

    def create(self , validated_data):
        self.delete()
        created_exchanges = []
        for data in validated_data['exchanges']:
           exchange =  ExchangeSerializer.create(self,data)
           created_exchanges.append(ExchangeSerializer(exchange).data)
        return {'exchanges': created_exchanges}


class ServerIpAddressSerializer(serializers.Serializer):
    ip_address = serializers.CharField(read_only= True)

    def create(self , validated_data):
        host = socket.gethostname()
        ip_addr = socket.gethostbyname(host)
        validated_data['ip_address'] = ip_addr
        return validated_data  
      




    
