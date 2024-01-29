from django.urls import path
from . import views

urlpatterns = [
    path('list-create/' , views.StrategyListCreateApiView.as_view() , name = 'strategy-list-create'),
    path('<int:pk>/' , views.StrategyRetrieveUpdateDestroyAPIView.as_view() , name = 'strategy-retrieve-update-destroy'),
    path('summery/' , views.ShortStrategyApiView.as_view() , name = 'strategy-summery'),
]