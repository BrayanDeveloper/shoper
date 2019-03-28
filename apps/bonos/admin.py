from django.contrib import admin
from apps.bonos.models import Bono

# Register your models here.
class BonoDisplay(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'puntos', 'fecha_bono')
	list_filter = ('nombre', 'fecha_bono')



admin.site.register(Bono,BonoDisplay)