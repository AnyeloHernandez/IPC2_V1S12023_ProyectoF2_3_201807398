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
    path('cartelera/', views.ver_cartelera, name='cartelera'),
    path('salas/', views.administrar_salas, name='administrar_salas'),
    path('salas/crear/', views.crear_sala, name='crear_sala'),
    path('salas/eliminar/<sala>', views.eliminar_sala, name='eliminar_sala'),
    path('salas/editar/<sala>', views.modificar_sala, name='modificar_sala'),
    path('comprar_boletos/<str:titulo>/', views.comprar_boletos, name='comprar_boletos'),
    path('comprar_boletos/<str:titulo>/mostrar_factura', views.mostrar_factura, name='mostrar_factura'),
    path('historial_boletos/', views.historial_boletos, name='historial_boletos'),
    path('favorito/<str:titulo>', views.pelicula_favorita, name='favorito'),
    path('peliculas_favoritas/', views.ver_peliculas_favoritas, name='peliculas_favoritas'),
    path('eliminar_favorito/<str:titulo>/', views.eliminar_favorito, name='eliminar_favorito'),
    path('cartelera/filtrar/<str:categoria>', views.filtrar_categoria, name='filtrar')
]