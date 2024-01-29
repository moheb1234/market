from rest_framework import serializers
from.models import Bot , Asset
from strategy.serializers import StrategySerializer
from exchange.serializer import ExchangeSerializer
from django.forms.models import model_to_dict
from .managers import bot_create


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__' 


class BotSerializer(serializers.ModelSerializer):
    strategy = StrategySerializer(read_only=True)
    exchange = ExchangeSerializer(read_only=True)
    asset_list_names = AssetSerializer(many = True , allow_null=True , required=False)
    

    class Meta:
        model = Bot
        fields = '__all__'
        extra_kwargs = {
        'exchange':{'write_only':True} ,
        'strategy':{'write_only':True}
    }
 
    def create(self , validated_data):
        strategy_id = self.context['view'].kwargs['str_id']
        exchange_id = self.context['view'].kwargs['ex_id']
        return bot_create(strategy_id , exchange_id , **validated_data)
