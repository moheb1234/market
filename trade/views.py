from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

class OrderListCreateApiView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
