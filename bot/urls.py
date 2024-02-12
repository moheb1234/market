from django.urls import path
from . import views

urlpatterns = [
    path('create' , views.BotCreateApiView.as_view() , name = 'bot-create')
]