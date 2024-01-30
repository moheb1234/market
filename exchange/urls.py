from django.urls import path
from . import views


urlpatterns = [
    path('list-save/' , views.ExchangeListSaveApiView.as_view() , name = 'exchange-list-save')
]