from indicator.models import *
from .models import Strategy
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
import json


def check_ind(ind_dict):
    if ind_dict['settings']['ind'] == 'MACD' :
        del ind_dict['settings']['ind']
        macd = MACD.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return macd
    if ind_dict['settings']['ind'] == 'RSI' :
        del ind_dict['settings']['ind']
        rsi = RSI.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return rsi
    if ind_dict['settings']['ind'] == 'RSICross' :
        del ind_dict['settings']['ind']
        rsi_cross = RSICross.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return rsi_cross
    if ind_dict['settings']['ind'] == 'RSIMa' :
        del ind_dict['settings']['ind']
        rsi_ma = RSIMa.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return rsi_ma
    if ind_dict['settings']['ind'] == 'MA' :
        del ind_dict['settings']['ind']
        ma = MA.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return ma
    if ind_dict['settings']['ind'] == 'OBV' :
        del ind_dict['settings']['ind']
        obv = OBV.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return obv
    if ind_dict['settings']['ind'] == 'STD' :
        del ind_dict['settings']['ind']
        std = STD.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return std
    if ind_dict['settings']['ind'] == 'Stochastic' :
        del ind_dict['settings']['ind']
        stochastic = Stochastic.objects.create(**ind_dict['settings'])
        del ind_dict['settings']
        return stochastic 



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
                setting = check_ind(open_ind)
                ind =  Indicator.objects.create(**open_ind)
                setting.indicator = ind
                setting.save()
                ind.open_str = strategy
                ind.save()

        if len(close_indicators) > 0:
            for close_ind in close_indicators:
                setting = check_ind(close_ind) 
                ind =  Indicator.objects.create(**close_ind)
                setting.indicator = ind
                setting.save()
                ind.close_str = strategy
                ind.save()
        return strategy


