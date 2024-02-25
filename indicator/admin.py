from django.contrib import admin
from .models import *

admin.site.register(Indicator)
admin.site.register(Setting)
admin.site.register(MACD)
admin.site.register(RSI)
admin.site.register(RSICross)
admin.site.register(RSIMa)
admin.site.register(MA)
admin.site.register(OBV)
admin.site.register(STD)
admin.site.register(Stochastic)

