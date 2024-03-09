from django.urls import path
from . import views

urlpatterns = [
    path('list-create/<str:bot_type>' , views.BotCreateApiView.as_view() , name = 'bot-list-create')
]