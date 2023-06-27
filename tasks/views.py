from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from models.carga_xml import *
from django.views.defaults import permission_denied

global lista_doble_ciruclar, lista_enlazada_usuarios

lista_enlazada_usuarios = cargar_usuarios_xml()
lista_doble_ciruclar_peliculas = cargar_peliculas_xml()

# Create your views here.
def home(request):
    lista_doble_ciruclar_peliculas = cargar_peliculas_xml()
    print(lista_enlazada_usuarios.usuario_logeado)
    # lista_doble_ciruclar_peliculas.imprimir_lista("2", None)
    if lista_enlazada_usuarios.usuario_logeado != '':
        return render(request, 'home.html', {
            "usuario": lista_enlazada_usuarios.usuario_logeado,
            "peliculas": lista_doble_ciruclar_peliculas
        })
    else:
        return render(request, 'home.html', {
            "usuario": 'Iniciar Sesión',
            "peliculas": lista_doble_ciruclar_peliculas
        })
    
def logout(request):
    lista_enlazada_usuarios.usuario_logeado = ''
    return redirect('home')

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
        # Se obtiene el rol desde el metodo login de la clase lista enlazada
        rol = lista_enlazada_usuarios.login(request.POST['correo'], request.POST['password'])
        if rol == 1:
            print("Se inicio sesion como administrador")
            return redirect('menu_administrador') # Menu administrador
        elif rol == 2:
            print("Se inicio sesion como cliente")
            # return HttpResponse(f'Se ingreso como cliente {lista_enlazada_usuarios.usuario_logeado}') # Menu cliente
            return redirect('home')
        else:
            return render(request, 'login.html', {
                "error": 'Usuario y contraseña no encontrados'
            })
        
def menu_administrador(request):
    #print(lista_enlazada_usuarios.usuario_logeado or "nada") 
    #print(lista_enlazada_usuarios.rol_logeado or "nada")
    if lista_enlazada_usuarios.rol_logeado == "administrador":
        if request.method == 'GET':
            return render(request, 'admin.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado
            })
    else:
        return permission_denied(request, "error")
    
def administrar_usuarios(request):
    if request.method == 'GET':
        return render(request, 'user_administration.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
            "usuarios": lista_enlazada_usuarios
        })
    
def ver_cartelera(request):
    if request.method == 'GET':
        return render(request, 'cartelera.html', {
            "usuario": lista_enlazada_usuarios.usuario_logeado,
            "peliculas": lista_doble_ciruclar_peliculas
        })
    
def administrar_peliculas(request):
    print(lista_enlazada_usuarios.usuario_logeado)
    print(lista_enlazada_usuarios.rol_logeado)
    lista_doble_ciruclar_peliculas = cargar_peliculas_xml()
    if request.method == 'GET':
        return render(request, 'movies_administration.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
            "peliculas": lista_doble_ciruclar_peliculas
        })
    
def eliminar_peliculas(request, titulo):
    print("eliminando pelicula")
    pelicula_eliminada = lista_doble_ciruclar_peliculas.delete(titulo)
    if pelicula_eliminada == 1:
        eliminar_pelicula_xml(titulo)
        print(f"Se elimino la pelicula: {titulo}")
        return render(request, 'movies_administration.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
            "peliculas": lista_doble_ciruclar_peliculas
        })
    else:
        return render(request, 'movies_administration.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
            "peliculas": lista_doble_ciruclar_peliculas
        })
    
def editar_peliculas(request, titulo):
    if request.method == 'GET':
        return render(request, 'editar_pelicula.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                "peliculas": lista_doble_ciruclar_peliculas
            })
    else:
        #try:
        categoria = request.POST['categoria']
        titulo_editado = request.POST['titulo']
        director = request.POST['director']
        imagen = request.POST['imagen']
        anno = request.POST['anno']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        print(categoria)
        print(titulo)
        print(director)
        print(imagen)
        print(anno)
        print(fecha)
        print(hora)
        cate, index = lista_doble_ciruclar_peliculas.editar_peliculas(
            categoria, titulo, titulo_editado, director, imagen, anno, fecha, hora)
        lista_doble_ciruclar_peliculas.imprimir_lista(2, None)
        modificar_pelicula_xml(cate, index)

        return redirect('administrar_peliculas')
        # except:
        #     return render(request, 'crear_pelicula.html', {
        #         "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
        #         "peliculas": lista_doble_ciruclar_peliculas,
        #         "error": 'Ocurrio un error'
        #     })

def eliminar_usuarios(request, correo):
    print(correo)
    usuario_eliminado = lista_enlazada_usuarios.delete(correo)
    if usuario_eliminado == 1:
        eliminar_usuario_xml(correo)
        print(f"Usuario {correo} eliminado.")
        return render(request, 'user_administration.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                "usuarios": lista_enlazada_usuarios
            })
    else:
        print("No se encontro el usuario")

def crear_usuarios(request):
    if request.method == 'GET':
        return render(request, 'crear_usuario.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
        })
    else:
        try:
            rol = request.POST['rol']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            telefono = request.POST['telefono']
            correo = request.POST['correo']
            if request.POST['password1'] == request.POST['password2']:
                contrasenna = request.POST['password1']
            
            # Se instancia el objeto
            nuevo_usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasenna)
            # Y se añade a la lista y luego al xml
            lista_enlazada_usuarios.add(nuevo_usuario)
            nuevo_usuario_xml(nombre, apellido, telefono, correo, contrasenna)
            return render(request, 'user_administration.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
            "usuarios": lista_enlazada_usuarios,
            "mensaje": 'Usuario Creado'
        })
        except:
            return render(request, 'crear_usuario.html', {
                    "error": 'Usuario ya existe'
                })

def editar_usuarios(request, correo):
    if request.method == 'GET':
        return render(request, 'editar_usuario.html', {
            "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
        })
    else:
        try:
            rol = request.POST['rol']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            telefono = request.POST['telefono']
            correo_editado = request.POST['correo']
            contrasenna = request.POST['password1']
            if (rol or nombre or apellido or telefono or correo_editado or contrasenna) == "":
                return render(request, 'editar_usuario.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                "usuarios": lista_enlazada_usuarios,
                "error": 'No deje espacios en blanco'
            })
            usuario, index = lista_enlazada_usuarios.editar_usuario(correo, correo_editado, rol, nombre, apellido, telefono, contrasenna)
            modificar_usuarios_xml(usuario, index)
            print(f"Se edito el usuario {correo}")
            return render(request, 'user_administration.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                "usuarios": lista_enlazada_usuarios
            })
        except:
            return render(request, 'editar_usuario.html', {
                "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                "usuarios": lista_enlazada_usuarios,
                "error": 'No deje espacios en blanco'
            })

def crear_peliculas(request):
            if request.method == 'GET':
                return render(request, 'crear_pelicula.html', {
                        "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                    })
            else:
                try:    
                    categoria = request.POST['categoria']
                    titulo = request.POST['titulo']
                    director = request.POST['director']
                    imagen = request.POST['imagen']
                    anno = request.POST['anno']
                    fecha = request.POST['fecha']
                    hora = request.POST['hora']
                    print(fecha)
                    print(hora)
                    print(imagen)
                    registro = nueva_pelicula_xml(categoria, titulo, director, imagen, anno, fecha, hora)
                    if registro == 1:
                        pelicula = Pelicula(titulo, director, imagen, anno, fecha, hora)
                        cate = Categoria(categoria, pelicula)
                        lista_doble_ciruclar_peliculas.add(cate)
                    return render(request, 'movies_administration.html', {
                        "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                        "peliculas": lista_doble_ciruclar_peliculas,
                        "mensaje": 'Pelicula creada'
                    })
                except:
                    return render(request, 'crear_pelicula.html', {
                        "usuario_logeado": lista_enlazada_usuarios.usuario_logeado,
                        "peliculas": lista_doble_ciruclar_peliculas,
                        "error": 'Ocurrio un error'
                    })