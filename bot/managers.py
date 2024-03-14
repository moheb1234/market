from exchange.models import Exchange

from strategy.models import Strategy

from .models import Bot , Asset

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import NotFound , ValidationError
import json

from rest_framework.exceptions import PermissionDenied




def bot_create(**validated_data):

    exchanges = validated_data['market_accounts']
    del validated_data['market_accounts']


    asset_list_names = json.loads(json.dumps((validated_data['asset_name'])))
    del validated_data['asset_name']

    strategy = validated_data['strategy']

    print(strategy.user)
    print(validated_data['user'])
    #check strategy owner
    if strategy.user != validated_data['user']:
        raise PermissionDenied({'detail' : 'this strategy is not for you'})

    #check exchanges owner
    for exchange in exchanges:
        if exchange.user != validated_data['user']:
            raise PermissionDenied({'detail' : f'you have not permission to use exchange {exchange.id}'})
      

    bot = Bot.objects.create(**validated_data)

    for exchange in exchanges:
        bot.market_accounts.add(exchange)
        bot.save()

    for asset in asset_list_names:
        as_obj = Asset.objects.create(**asset)
        as_obj.bot = bot
        as_obj.save()
        
    return bot



