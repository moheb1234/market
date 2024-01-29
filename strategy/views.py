from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStrategyOwner
from .serializers import StrategySerializer , ShortStrategySerializer
from .models import Strategy

class StrategyListCreateApiView(generics.ListCreateAPIView):
    serializer_class = StrategySerializer
    permission_classes = [IsAuthenticated] 
    def get_queryset(self):
        return Strategy.objects.filter(user= self.request.user)


class ShortStrategyApiView(generics.ListAPIView):
    serializer_class = ShortStrategySerializer
    permission_classes = [IsAuthenticated]   
    def get_queryset(self):
        return Strategy.objects.filter(user= self.request.user)


class StrategyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StrategySerializer
    permission_classes = [IsAuthenticated , IsStrategyOwner]
    queryset = Strategy.objects.all()

