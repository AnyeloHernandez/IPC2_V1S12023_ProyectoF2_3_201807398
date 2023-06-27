"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', views.menu_administrador, name='menu_administrador'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('usuarios/', views.administrar_usuarios, name='administrar_usuarios'),
    path('peliculas/', views.administrar_peliculas, name='administrar_peliculas'),
    path('peliculas/eliminar/<str:titulo>', views.eliminar_peliculas, name='eliminar_pelicula'),
    path('peliculas/crear/', views.crear_peliculas, name='crear_pelicula'),
    path('peliculas/editar/<str:titulo>', views.editar_peliculas, name='editar_pelicula'),
    path('usuarios/eliminar/<str:correo>', views.eliminar_usuarios, name='eliminar_usuario'),
    path('usuarios/crear/', views.crear_usuarios, name='crear_usuario'),
    path('usuarios/editar/<str:correo>', views.editar_usuarios, name='editar_usuario'),
    path('cartelera/', views.ver_cartelera, name='cartelera')
]
