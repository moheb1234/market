from exchange.models import Exchange



from strategy.models import Strategy



from .models import Bot , Asset



from django.core.exceptions import ObjectDoesNotExist



from rest_framework.exceptions import NotFound
import json




def bot_create(**validated_data):

    try:
        strategy = Strategy.objects.get(pk = validated_data['strategy_id'])
    except ObjectDoesNotExist:
        raise NotFound(detail={'detail':'no strategy founded'})
    try:
        exchange = Exchange.objects.get(pk = validated_data['exchange_id'])
    except ObjectDoesNotExist:
        raise NotFound(detail={'detail':'no exchange founded'})

    validated_data['strategy'] = strategy
    validated_data['exchange'] = exchange

    asset_list_names = json.loads(json.dumps((validated_data['asset_list_names'])))
    del validated_data['asset_list_names']

    bot = Bot.objects.create(**validated_data)

    for asset in asset_list_names:
        as_obj = Asset.objects.create(**asset)
        bot.asset_list_names.add(as_obj)
        bot.save()
        
    return bot



