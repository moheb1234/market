from django.db.models.signals import pre_delete
from django.dispatch import receiver
from indicator.models import Indicator
from .models import Strategy

@receiver(pre_delete , sender = Strategy)
def handler(sender , **kwargs):
    strategy =  kwargs['instance']
    open_indicators = Indicator.objects.filter(open_str= strategy)
    for ind in open_indicators:
        ind.delete()
    
    close_indicators = Indicator.objects.filter(close_str= strategy)
    for ind in close_indicators:
        ind.delete()