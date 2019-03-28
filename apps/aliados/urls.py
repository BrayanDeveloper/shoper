from django.urls import path, include
from apps.aliados.views import index_aliados
urlpatterns = [
    path('', index_aliados),
]
