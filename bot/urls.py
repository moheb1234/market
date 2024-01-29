from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:str_id>/<int:ex_id>/' , views.BotCreateApiView.as_view() , name = 'bot-create')
]