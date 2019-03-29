from django.urls import path, include
from apps.viajes.views import index_viajes, registro_planes, registro_hoteles, registro_autos, registro_actividades
urlpatterns = [
    path('', index_viajes, name="index_viajes"),
    path('registro_vuelos/', index_viajes, name="registro_vuelos"),
    path('registro_planes/', registro_planes, name="registro_planes"),
    path('registro_hoteles/', registro_hoteles, name="registro_hoteles"),
    path('registro_autos/', registro_autos, name="registro_autos"),
    path('registro_actividad/', registro_actividades, name="registro_actividad"),
]

