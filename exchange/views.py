from rest_framework import generics
from .serializer import ExchangeBulkSaveSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Exchange

class ExchangeListSaveApiView(generics.ListCreateAPIView):
    serializer_class = ExchangeBulkSaveSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Exchange.objects.filter(user = self.request.user)
