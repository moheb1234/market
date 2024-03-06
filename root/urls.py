
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('strategy/', include('strategy.urls')),
    path('user/', include('users.urls')),
    path('exchange/', include('exchange.urls')),
    path('bot/', include('bot.urls')),
    path('export/', include('export.urls')),
    path('news/', include('news.urls')),
] +static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
