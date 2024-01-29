from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bot
from .serializers import BotSerializer


class BotCreateApiView(generics.CreateAPIView):
    serializer_class = BotSerializer
    permission_classes = [IsAuthenticated]
    queryset = Bot.objects.all()
