from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('signin/',views.signin,name='signin'),
    path('service/',views.service, name='service'),
    path('jason/',views.jason, name='p1'),
    path('chucky/',views.chucky, name='p2'),
    path('freddy/', views.freddy, name='p3'),
    path('annabelle/', views.annabelle, name='p4'),
    path('menu/', views.menu, name='menu'),
    path('profile/edit/', views.profile_edit,name='profile_edit'),
    
    path('menu/movie/add', views.MovieCreateView.as_view(), name='add_movie'),
    path('menu/movie/', views.MovieListView.as_view(), name='list_movie'),
    path('menu/movie/<int:pk>/detail', views.MovieDetailView.as_view(), name='detail_movie'),
    path('menu/movie/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='edit_movie'),
    path('menu/movie/<int:pk>/del/', views.MovieDeleteView.as_view() ,name='delete_movie'),

     
]
