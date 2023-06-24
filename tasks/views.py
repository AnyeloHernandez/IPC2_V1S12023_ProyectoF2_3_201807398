from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from models.carga_xml import *

global lista_doble_ciruclar, lista_enlazada_usuarios

lista_enlazada_usuarios = cargar_usuarios_xml()
lista_doble_ciruclar_peliculas = cargar_peliculas_xml()

# Create your views here.
def home(request):
    lista_doble_ciruclar_peliculas = cargar_peliculas_xml()
    # lista_doble_ciruclar_peliculas.imprimir_lista("2", None)
    if lista_enlazada_usuarios.usuario_logeado != '':
        return render(request, 'home.html', {
            "usuario": f'Bienvenido {lista_enlazada_usuarios.usuario_logeado}',
            "peliculas": lista_doble_ciruclar_peliculas
        })
    else:
        print(type(lista_doble_ciruclar_peliculas))
        return render(request, 'home.html', {
            "peliculas": lista_doble_ciruclar_peliculas
        })

def signup(request):
    #lista_enlazada_usuarios.imprimir_lista()
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        # print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Revisa que no hayan inputs vacios
                for valor in request.POST.values():
                    # print(valor)
                    if not valor:
                        return render(request, 'signup.html', {
                    "error": 'No deje elementos vacios'
                })
                correo = request.POST['correo']
                contrasenna = request.POST['password1']
                nombre = request.POST['nombre']
                apellido = request.POST['apellido']
                telefono = request.POST['telefono']
                # Se instancia el objeto
                nuevo_usuario = Usuario('cliente', nombre, apellido, telefono, correo, contrasenna)
                # Y se añade a la lista y luego al xml
                lista_enlazada_usuarios.add(nuevo_usuario)
                nuevo_usuario_xml(nombre, apellido, telefono, correo, contrasenna)
                return redirect('login')
            except:
                return render(request, 'signup.html', {
                    "error": 'Usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                "error": 'Las contraseñas no coinciden'
            })

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        rol = lista_enlazada_usuarios.login(request.POST['correo'], request.POST['password'])
        if rol == 1:
            print("Se inicio sesion como administrador")
            return HttpResponse('Se ingreso como administrador') # Menu administrador
        elif rol == 2:
            print("Se inicio sesion como cliente")
            # return HttpResponse(f'Se ingreso como cliente {lista_enlazada_usuarios.usuario_logeado}') # Menu cliente
            return redirect('home')
        else:
            return render(request, 'login.html', {
                "error": 'Usuario y contraseña no encontrados'
            })