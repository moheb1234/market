from exchange.models import Exchange

from strategy.models import Strategy

from .models import Bot , Asset

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import NotFound , ValidationError
import json




def bot_create(**validated_data):

    # try:
    #     strategy = Strategy.objects.get(pk = validated_data['strategy_id'])
    # except ObjectDoesNotExist:
    #     raise NotFound(detail={'detail':'no strategy founded'})

    exchanges = validated_data['market_accounts']
    del validated_data['market_accounts']
    
    # validated_data['strategy'] = strategy


    asset_list_names = json.loads(json.dumps((validated_data['asset_name'])))
    del validated_data['asset_name']

    bot = Bot.objects.create(**validated_data)

    for exchange in exchanges:
        bot.market_accounts.add(exchange)
        bot.save()

    for asset in asset_list_names:
        as_obj = Asset.objects.create(**asset)
        as_obj.bot = bot
        as_obj.save()
        
    return bot



