from django.shortcuts import render
from apps.viajes.models import Vuelo, Plan, Hotel, Auto, Actividad
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


	return render(request, 'viajes/index.html', {'registroVuelo':'registro Exitoso del Vuelo'})

def registro_planes(request):
	if request.method == "POST":
		desde = request.POST.get('desde')
		donde = request.POST.get('donde')
		cuando_viajas = request.POST.get('cuando_viajas')
		cuando_vuelves = request.POST.get('cuando_vuelves')
		habitaciones = request.POST.get('habitaciones')
		adultos = request.POST.get('adultos')
		ninos = request.POST.get('ninos')

		registro = Plan(desde=desde, hasta=donde, cuando_viaja=cuando_viajas, cuando_vuelve=cuando_vuelves, numero_habitaciones=habitaciones, numero_adultos=adultos, numero_ninos=ninos)
		registro.save()


	return render(request, 'viajes/index.html', {'registroPlan':'registro Exitoso del plan'})

def registro_hoteles(request):
	if request.method == "POST":
		donde = request.POST.get('donde')
		cuando_llegas = request.POST.get('cuando_llegas')
		cuando_sales = request.POST.get('cuando_sales')
		habitaciones = request.POST.get('habitaciones')
		adultos = request.POST.get('adultos')
		ninos = request.POST.get('ninos')

		registro = Hotel(donde=donde, cuando_llegas=cuando_llegas, cuando_sales=cuando_sales, numero_habitaciones=habitaciones, numero_adultos=adultos, numero_ninos=ninos)
		registro.save()


	return render(request, 'viajes/index.html', {'registroHotel':'registro Exitoso del Hotel'})

def registro_autos(request):
	if request.method == "POST":
		recoger = request.POST.get('recoger')
		entregar = request.POST.get('entregar')
		cuando_llegas = request.POST.get('cuando_llegas')
		hora_salida = request.POST.get('hora_salida')
		cuando_entregas = request.POST.get('cuando_entregas')
		hora_entrega = request.POST.get('hora_entrega')

		registro = Auto(recoger=recoger, entregar=entregar, cuando_llegas=cuando_llegas, hora_salida=hora_salida, cuando_entregas=cuando_entregas, hora_entrega=hora_entrega)
		registro.save()


	return render(request, 'viajes/index.html', {'registroAutos':'registro Exitoso del Auto'})

def registro_actividades(request):
	if request.method == "POST":
		hacia = request.POST.get('hacia')
		cuando_llegas = request.POST.get('cuando_llegas')
		cuando_regresas = request.POST.get('cuando_regresas')

		registro = Actividad(hacia_donde=hacia, cuando_llegas=cuando_llegas, cuando_regresas=cuando_regresas)
		registro.save()


	return render(request, 'viajes/index.html', {'registroActividades':'registro Exitoso de la Actividad'})