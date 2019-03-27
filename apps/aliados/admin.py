from django.contrib import admin
from apps.aliados.models import Aliado
# Register your models here.

class DisplayAliado(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'thumbnail', 'fecha_aliado')

admin.site.register(Aliado, DisplayAliado)