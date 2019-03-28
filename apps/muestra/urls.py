from django.urls import path, include
from apps.muestra.views import index, muestra1, muestra2
urlpatterns = [
    path('', index),
    path('muestra1/', muestra1),
    path('muestra2/', muestra2),
]
