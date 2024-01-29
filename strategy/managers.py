from indicator.models import Setting,Indicator
from .models import Strategy
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
import json


def strategy_create( **validated_data ):
        open_indicators = json.loads(json.dumps((validated_data['open'])))
        close_indicators = json.loads(json.dumps((validated_data['close'])))

        del validated_data['open']
        del validated_data['close']

        try:
            strategy =  Strategy.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError({'details':'strategy name is duplicate please chose an other name'})

        for open_ind in open_indicators:
            settings = Setting.objects.create(**open_ind['settings'])
            del open_ind['settings']
            ind =  Indicator.objects.create(**open_ind)
            ind.settings = settings
            ind.open_str = strategy
            ind.save()

        if len(close_indicators) > 0:
            for close_ind in close_ind:
                settings = Setting.objects.create(**open_ind['settings'])
                del close_ind['settings']
                ind =  Indicator.objects.create(**close_ind)
                ind.settings = settings
                ind.close_str = strategy
                ind.save()
                
        return strategy