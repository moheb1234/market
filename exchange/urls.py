from django.urls import path
from . import views


urlpatterns = [
    path('list-create/' , views.ExchangeListCreateApiView.as_view() , name = 'exchange-list-create')
]