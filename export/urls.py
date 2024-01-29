from django.urls import path 
from . import views

urlpatterns = [
    path('create/' , views.ExportCreateApiView.as_view() , name = 'export-create')
]