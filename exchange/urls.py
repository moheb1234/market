from django.urls import path
from . import views


urlpatterns = [
    path('bulk-save' , views.ExchangebulkSaveApiView.as_view() , name = 'exchange-bulk-save'),
    path('list' , views.ExchangeListApiView.as_view() , name = 'exchange-list')
]