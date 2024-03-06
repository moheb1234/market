from .serializers import NewsSerializer
from rest_framework import generics
from .models import News


class NewsListCreateApiView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

