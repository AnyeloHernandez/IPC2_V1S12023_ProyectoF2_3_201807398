from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from models.carga_xml import *

lista_enlazada_usuarios = cargar_usuarios_xml()
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    lista_enlazada_usuarios.imprimir_lista()
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
            except:
                return HttpResponse('username already exists')
        else:
            return HttpResponse('Password do not match')
        
    # Hacer todo en este archivo que chingados jeje