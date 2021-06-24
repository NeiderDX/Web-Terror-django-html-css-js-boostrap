import json
import requests
from core.models import Movie, User
from core.forms import MovieAddForm, ProfileEditForm, UsersCreationForm
from django.shortcuts import redirect, render, get_object_or_404

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
    respone=requests.get('https://imdb-api.com/en/API/Title/k_29bfmsvl/'+pk,params={})
    result=json.loads(respone.text)
    user=User.objects.get(email=request.user.email)
    if request.method=="POST":
        form=MovieAddForm(request.POST)
        form.save(user,result['id'],result['title'],result['releaseDate'],result['runtimeStr'],result['imDbRating'])
        return redirect('menu')
    return render(request, 'core/mostrar_pelicula.html',{'movie':result})

def profile_edit(request):
    usuario=get_object_or_404(User, email=request.user.email)
    if request.method=='POST':
       form=ProfileEditForm(request.POST, instance=usuario)
       if form.is_valid():
           form.save()
           return redirect('index')
    else:
        datos={
        'form':ProfileEditForm(instance=usuario),
      
    }
    if request.user.is_authenticated==True:
        return render(request, 'core/modificar.html',datos)
    else:
        return redirect('login')

def movie_delete(request,pk):
    user=User.objects.get(email=request.user.email)
    movie=get_object_or_404(Movie,user_id=user.id, id=pk)
    movie.delete()
    return redirect('favorites')

def listar_peliculas(request):
    # queryset   ..... SELECT * FROM CARRERA
    user=User.objects.get(email=request.user.email)
    movies = Movie.objects.filter(user_id=user.id).all()
    return render(request, "core/listar_peliculas.html", {'movies': movies})



