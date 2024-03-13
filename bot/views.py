from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bot
from .permissions import IsBotOwner
from .serializers import BotSerializer , BotEventSerializer
from rest_framework.exceptions import NotFound


class BotCreateApiView(generics.ListCreateAPIView):
    serializer_class = BotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bot_type = self.kwargs['bot_type']
        return Bot.objects.filter(strategy__user = self.request.user  , bot_type= bot_type)
        

class BotRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotSerializer
    permission_classes = [IsAuthenticated , IsBotOwner]
    queryset = Bot.objects.all()

class BotEventApiView(generics.UpdateAPIView):
    serializer_class = BotEventSerializer
    permission_classes = [IsAuthenticated , IsBotOwner]
    queryset = Bot.objects.all()

