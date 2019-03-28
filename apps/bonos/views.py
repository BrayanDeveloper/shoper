from django.shortcuts import render
from apps.bonos.models import Bono
# Create your views here.
def index_bonos(request):
	bonos = Bono.objects.all()
	return render(request, 'bonos/index.html', {'bonos':bonos})