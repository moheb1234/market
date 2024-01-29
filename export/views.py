from rest_framework import generics
from .serializers import ExportSerializer
from .models import Export


class ExportCreateApiView(generics.CreateAPIView):
    serializer_class = ExportSerializer
    queryset = Export.objects.all()
