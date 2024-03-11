from django.urls import path

from . import views


urlpatterns = [

    path('list-create/<str:bot_type>' , views.BotCreateApiView.as_view() , name = 'bot-list-create'),

    path('<int:pk>' , views.BotRetrieveUpdateDestroyApiView.as_view() , name = 'bot-retrieve-update-delete'),

    path('event/<int:pk>' , views.BotEventApiView.as_view() , name = 'bot-event'),

]