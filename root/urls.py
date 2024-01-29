
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('strategy/', include('strategy.urls')),
    path('user/', include('users.urls')),
    path('exchange/', include('exchange.urls')),
    path('bot/', include('bot.urls')),
    path('export/', include('export.urls')),
]
