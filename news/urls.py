from django.urls import path
from . import views

urlpatterns = [
    path('save/<str:category>' , views.NewsBulkSaveApiView.as_view() , name = 'news-save') ,
    path('fetch/<str:category>' , views.NewsListApiView.as_view() , name = 'news-fetch')
]