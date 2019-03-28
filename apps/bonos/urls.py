from django.urls import path, include
from apps.bonos.views import index_bonos
urlpatterns = [
    path('', index_bonos, name="index_bonos"),
]
