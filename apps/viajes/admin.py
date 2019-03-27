from django.contrib import admin
from apps.viajes.models import Vuelo, Plan, Hotel, Auto, Actividad
# Register your models here.

admin.site.register(Vuelo)
admin.site.register(Plan)
admin.site.register(Hotel)
admin.site.register(Auto)
admin.site.register(Actividad)