from rest_framework import generics
from .serializers import HireRepresentSerializer , SupportSerializer , SignalPartnerSerializer
from .models import Signal , Hire , Support
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrCreateOnly



class SignalPartnerListCreateApiView(generics.ListCreateAPIView):
    serializer_class = SignalPartnerSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        object_type = self.kwargs['type']
        user = self.request.user
        return Signal.objects.filter(user= user , object_type=object_type)



class HireRepresentListCreateApiView(generics.ListCreateAPIView):
    serializer_class = HireRepresentSerializer
    permission_classes = [IsAdminOrCreateOnly]
    def get_queryset(self):
        object_type = self.kwargs['type']
        return Hire.objects.filter(object_type=object_type)

class SupportListCreateApiView(generics.ListCreateAPIView):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()
    permission_classes = [IsAdminOrCreateOnly]