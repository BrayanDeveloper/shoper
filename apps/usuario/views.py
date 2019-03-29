from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
	if request.method == "POST":
		user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
		if user is not None:
			return redirect('/usuario')
		else:
			return render(request, 'login/login.html', {'respuesta': 'no eres un usuario Registrado'})
	return render(request, 'login/login.html')



def usuario(request):
	return render(request, 'usuarios/index.html')

#@login_required(login_url="/login")
#def logout_view(request):
#    logout(request)
#    return redirect('/login')

