from indicator.models import Setting,Indicator ,MACD
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
            raise ValidationError({'detail':'strategy name is duplicate please chose an other name'})
        if len(open_indicators) > 0:
            for open_ind in open_indicators:
                if open_ind['name'] == 'Moving Average Convergence Divergence (MACD)' :
                    del open_ind['settings']['resourcetype']
                    macd = MACD.objects.create(**open_ind['settings'])
                    del open_ind['settings']
                    ind =  Indicator.objects.create(**open_ind)
                    macd.indicator = ind
                    macd.save()
                    ind.open_str = strategy
                    ind.save()

        if len(close_indicators) > 0:
            for close_ind in close_indicators:
                if close_ind['name'] == 'Moving Average Convergence Divergence (MACD)':
                    del close_ind['settings']['resourcetype']
                    macd = MACD.objects.create(**close_ind['settings'])
                    del close_ind['settings']
                    ind =  Indicator.objects.create(**close_ind)
                    macd.indicator = ind
                    macd.save()
                    ind.close_str = strategy
                    ind.save()
        return strategy