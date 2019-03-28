from django.shortcuts import render
from apps.aliados.models import Aliado
# Create your views here.
def index_aliados(request):
	aliados = Aliado.objects.all()
	return render(request, 'aliados/index.html', {'aliados':aliados})