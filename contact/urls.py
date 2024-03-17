from django.urls import path
from . import views

urlpatterns = [
    path('support-us/list-create' , views.SupportListCreateApiView.as_view() , name = 'support-us-list-create'),
    path('signal-partner/list-create/<str:type>' , views.SignalPartnerListCreateApiView.as_view() , name = 'signal-partner-list-create'),
    path('hire-represent/list-create/<str:type>' , views.HireRepresentListCreateApiView.as_view() , name = 'hire-represent-list-create'),
]