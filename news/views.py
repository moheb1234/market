from .serializers import BulkNewsSerializer , NewsSerializer
from rest_framework import generics
from .models import News


class NewsBulkSaveApiView(generics.CreateAPIView):
    serializer_class = BulkNewsSerializer
    

class NewsListApiView(generics.ListAPIView):
    serializer_class = NewsSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return News.objects.filter(category=category)

