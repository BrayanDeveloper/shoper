from django.shortcuts import render
from apps.viajes.models import Vuelo
# Create your views here.
def index_viajes(request):
	if request.method == "POST":
		desde = request.POST.get('desde')
		donde = request.POST.get('donde')
		cuando_viajas = request.POST.get('cuando_viajas')
		cuando_vuelves = request.POST.get('cuando_vuelves')
		adultos = request.POST.get('adultos')
		ninos = request.POST.get('ninos')

		registro = Vuelo(desde=desde, hasta=donde, cuando_viaja=cuando_viajas, cuando_vuelve=cuando_vuelves, numero_adultos=adultos, numero_ninos=ninos)
		registro.save()


	return render(request, 'viajes/index.html', {'registro':'registro Exitoso'})