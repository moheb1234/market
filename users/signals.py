from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Users , Profile

@receiver(post_save, sender = Users)
def handler(sender , **kwargs):
    user = kwargs['instance']
    Profile.objects.get_or_create(user = user)