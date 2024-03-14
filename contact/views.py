from rest_framework import generics
from .serializers import HireSerializer , SupportSerializer
from .models import Signal , Hire , Support


class HireListCreateApiView(generics.ListCreateAPIView):
    serializer_class = HireSerializer
    queryset = Hire.objects.all()

class SupportListCreateApiView(generics.ListCreateAPIView):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()