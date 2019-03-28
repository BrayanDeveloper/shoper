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

class ListaDisplay(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'usuario')
	list_filter = ('nombre', 'tipo', 'usuario')
	search_fields = ['nombre', 'tipo', 'usuario']

class PuntoDisplay(admin.ModelAdmin):
	list_display = ('puntos', 'usuario', 'fecha_puntos')
	list_filter = ('puntos', 'usuario', 'fecha_puntos')
	search_fields = ['puntos', 'usuario', 'fecha_puntos']

class CompraDisplay(admin.ModelAdmin):
	list_display = ('compra', 'tipo', 'usuario', 'fecha_compra')
	list_filter = ('compra', 'tipo', 'usuario', 'fecha_compra')
	search_fields = ['compra', 'tipo', 'usuario', 'fecha_compra']

class CarritoDisplay(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'usuario', 'valor', 'fecha_carrito')
	list_filter = ('nombre', 'tipo', 'usuario', 'valor', 'fecha_carrito')
	search_fields = ['nombre', 'tipo', 'usuario', 'valor', 'fecha_carrito']


admin.site.register(Usuario, UsuarioDisplay)
admin.site.register(Notificacion, NotiDisplay)
admin.site.register(Puntos, PuntoDisplay)
admin.site.register(Compras, CompraDisplay)
admin.site.register(Lista_Favorito, ListaDisplay)
admin.site.register(Carrito, CarritoDisplay)