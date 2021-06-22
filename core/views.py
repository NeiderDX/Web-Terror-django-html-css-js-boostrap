import requests
from core.models import User
from core.forms import UsersCreationForm
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def signin(request):
    datos={
        'form':UsersCreationForm()
    }
    
    if request.method=="POST":
        formulario=UsersCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
            
    
    
    return render(request,'core/formulario.html',datos)

def menu(request):
    return render(request,'core/menu.html')

def service(request):
    return render(request,'core/servicio_web.html')

def jason(request):
    return render(request, 'core/p_1.html')

def chucky(request):
    return render(request,'core/p_2.html')

def freddy(request):
    return render(request,'core/p_3.html')

def annabelle(request):
    return render(request, 'core/p_4.html')

def redirect_login(request):
    return redirect('login')

def show_details(request,pk):
    return render(request, 'core/mostrar_pelicula.html')