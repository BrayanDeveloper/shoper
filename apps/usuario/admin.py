from django.contrib import admin
from apps.usuario.models import Usuario, Notificacion, Puntos, Compras, Lista_Favorito, Carrito
# Register your models here.

class UsuarioDisplay(admin.ModelAdmin):
	list_display = ('nombre', 'correo', 'telefono')
	list_filter = ('nombre', 'correo', 'telefono')
	search_fields = ['nombre', 'correo', 'telefono']

class NotiDisplay(admin.ModelAdmin):
	list_display = ('correo_electronico', 'mensaje_texto', 'llamada_telefonica', 'usuario')
	list_filter = ('usuario','correo_electronico')
	search_fields = ['usuario', 'correo_electronico']

admin.site.register(Usuario, UsuarioDisplay)
admin.site.register(Notificacion, NotiDisplay)
admin.site.register(Puntos)
admin.site.register(Compras)
admin.site.register(Lista_Favorito)
admin.site.register(Carrito)