from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bot
from .serializers import BotSerializer
from rest_framework.exceptions import NotFound


class BotCreateApiView(generics.ListCreateAPIView):
    serializer_class = BotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bot_type = self.kwargs['bot_type']
        if bot_type == 'trade':
            return Bot.objects.filter(strategy__user = self.request.user , start_date= None , end_date= None)
        elif bot_type == 'back-test':
            return Bot.objects.filter(strategy__user = self.request.user , start_date__isnull= False , end_date__isnull= False)
        else :
            raise NotFound({'detail' : 'url not found'})

