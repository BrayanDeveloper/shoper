from django.urls import path, include
from apps.viajes.views import index_viajes
urlpatterns = [
    path('', index_viajes, name="index_viajes"),
]
