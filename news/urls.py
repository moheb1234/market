from django.urls import path
from . import views

urlpatterns = [
    path('list-create' , views.NewsListCreateApiView.as_view() , name = 'news-list-create')
]