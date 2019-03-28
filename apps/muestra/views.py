from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'muestra/index.html')

def muestra1(request):
	return HttpResponse('muestra1')

def muestra2(request):
	return HttpResponse('muestra2')