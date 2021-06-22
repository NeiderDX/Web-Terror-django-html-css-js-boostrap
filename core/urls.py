from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/', views.redirect_login, name='logout'),
    path('signin/',views.signin,name='signin'),
    path('service/',views.service, name='service'),
    path('jason/',views.jason, name='p1'),
    path('chucky/',views.chucky, name='p2'),
    path('freddy/', views.freddy, name='p3'),
    path('annabelle/', views.annabelle, name='p4'),
    path('menu/', views.menu, name='menu'),
    path('menu/view/<str:pk>', views.show_details, name='show_movie')
]
