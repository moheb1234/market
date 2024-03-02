from rest_framework import generics
from .serializer import ExchangeBulkSaveSerializer ,ExchangeSerializer ,ServerIpAddressSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Exchange

class ExchangeBulkSaveApiView(generics.CreateAPIView):
    serializer_class = ExchangeBulkSaveSerializer
    permission_classes = [IsAuthenticated]
    queryset = Exchange.objects.all()
    
class ExchangeListApiView(generics.ListAPIView):
    serializer_class = ExchangeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exchange.objects.filter(user = self.request.user)


class ServerIpAddressApiView(generics.CreateAPIView):
    serializer_class = ServerIpAddressSerializer
    permission_classes = [IsAuthenticated]



    
