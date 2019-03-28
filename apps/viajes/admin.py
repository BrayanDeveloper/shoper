from django.contrib import admin
from apps.viajes.models import Vuelo, Plan, Hotel, Auto, Actividad
# Register your models here.


class VueloDisplay(admin.ModelAdmin):
	list_display = ('desde', 'hasta', 'fecha_vuelo')
	list_filter = ('fecha_vuelo',) 

class PlanDisplay(admin.ModelAdmin):
	list_display = ('desde', 'hasta', 'fecha_plan')
	list_filter = ('fecha_plan',) 

class HotelDisplay(admin.ModelAdmin):
	list_display = ('donde', 'cuando_llegas', 'fecha_hotel')
	list_filter = ('fecha_hotel'), 

class AutoDisplay(admin.ModelAdmin):
	list_display = ('recoger', 'entregar', 'fecha_auto')
	list_filter = ('fecha_auto',) 

class ActividadDisplay(admin.ModelAdmin):
	list_display = ('hacia_donde', 'cuando_llegas', 'fecha_actividad')
	list_filter = ('fecha_actividad',) 


admin.site.register(Vuelo,VueloDisplay)
admin.site.register(Plan,PlanDisplay)
admin.site.register(Hotel,HotelDisplay)
admin.site.register(Auto,AutoDisplay)
admin.site.register(Actividad,ActividadDisplay)