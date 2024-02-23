from django.urls import path
from . import views


urlpatterns = [
    path('bulk-save' , views.ExchangeBulkSaveApiView.as_view() , name = 'exchange-bulk-save'),
    path('list' , views.ExchangeListApiView.as_view() , name = 'exchange-list'),
    path('server-ipaddress' , views.ServerIpAddressApiView.as_view() , name = 'server-ip-address')
]