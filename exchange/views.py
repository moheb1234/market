from rest_framework import generics
from .serializer import ExchangeSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Exchange

class ExchangeListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ExchangeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Exchange.objects.filter(user = self.request.user)
    