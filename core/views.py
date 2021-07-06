from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework import generics
from .serializers import MovieSerializer
from core.models import Movie, User
from core.forms import MovieForm, ProfileEditForm, UsersCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
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

# details
# # def show_details(request,pk):
#     respone=requests.get('https://imdb-api.com/es/API/Title/k_fdn8m1c9/'+pk,params={})
#     result=json.loads(respone.text)
#     user=User.objects.get(email=request.user.email)
#     if request.method=="POST":
#         form=MovieAddForm(request.POST)
#         form.save(user,result['id'],result['title'],result['releaseDate'],result['runtimeStr'],result['imDbRating'])
#         return redirect('menu')
#     return render(request, 'core/mostrar_pelicula.html',{'movie':result})

# update
def profile_edit(request):
    usuario=get_object_or_404(User, email=request.user.email)
    if request.method=='POST':
       form=ProfileEditForm(request.POST, instance=usuario)
       if form.is_valid():
           form.save()
           return redirect('menu')
    else:
        datos={
        'form':ProfileEditForm(instance=usuario),
      
    }
    if request.user.is_authenticated==True:
        return render(request, 'core/modificar.html',datos)
    else:
        return redirect('login')

# delete
def movie_delete(request,pk):
    user=User.objects.get(email=request.user.email)
    movie=get_object_or_404(Movie,user_id=user.id, id=pk)
    movie.delete()
    return redirect('favorites')

# list
def listar_peliculas(request):
    # queryset   ..... SELECT * FROM CARRERA
    user=User.objects.get(email=request.user.email)
    movies = Movie.objects.filter(user_id=user.id).all()
    return render(request, "core/listar_peliculas.html", {'movies': movies})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request,'core/listar_peliculas.html', {'movies': movies})

# with generic 
class MovieListView(ListView):
    model = Movie
    template_name = "core/listar_peliculas.html"
    
    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)

class MovieUpdateView(UpdateView):
    model = Movie
    form_class=MovieForm
    template_name = "core/editar_pelicula.html"
    success_url=reverse_lazy('list_movie')
    
class MovieCreateView(CreateView):
    model = Movie
    form_class=MovieForm
    template_name = "core/añadir_pelicula.html"
    success_url=reverse_lazy('list_movie')
    def get_initial(self):
        return {
            "user": self.request.user
        }

class MovieDeleteView(DeleteView):
    model = Movie
    template_name="core/confirmar_eliminacion.html"
    success_url=reverse_lazy('list_movie')

class MovieDetailView(DetailView):
    model = Movie
    template_name = "core/mostrar_pelicula.html"
    
    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user)

# API objects
class API_objects(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class= MovieSerializer

class API_objects_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class= MovieSerializer
    
# auth_token for user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
