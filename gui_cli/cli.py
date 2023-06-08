from models.carga_xml import *

lista_enlazada_usuarios = cargar_usuarios_xml()


class Cli:
    global marco
    marco = "*" * 15

    def __init__(self):
        while True:
            self.menu_inicio()

    def menu_inicio_sesion(self):
        correo = input("Ingrese su correo: ")
        contrasenna = input("Ingrese su contraseña: ")
        lista_enlazada_usuarios.imprimir_lista()
        rol = lista_enlazada_usuarios.login(correo, contrasenna)
        if rol == 1:
            self.menu_administrador()
        elif rol == 2:
            self.menu_cliente()
        else:
            print("Inicio de sesion incorrecto")
        # todo: checkear si el usuario tiene rol de admin o no

    def menu_inicio(self):
        print(marco)
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        print(marco)

        opcion = input("Ingrese opcion: ")
        if opcion == "1": # Inicia sesión
            self.menu_inicio_sesion()
        elif opcion == "2": # Registrar usuario
            self.menu_registrar()
        elif opcion == "3": # Sale del sistema
            print("Se ha salido del sistema. Tenga un buen día.")
            exit()
        else:
            print("Ingrese una opción válida.")
        
    def menu_cliente(self):
        '''
        TODO: 
        Ver listado de peliculas en general
        Listado de peliculas favoritas del usuario
        Comprar boletos para la pelicula
        Historial de boletos
        '''
        print("menucliente")
        pass

    def menu_registrar(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = int(input("Ingrese su número de telefono: ")) # Revisar si se puede con str o int
        correo = input("Ingrese su correo: ")
        contrasenna = input("Ingrese su contraseña: ")
        # Instanciamos un nuevo usuario
        nuevo_usuario = Usuario('cliente', nombre, apellido, telefono, correo, contrasenna)
        # Lo cargamos en el XML
        nuevo_usuario_xml(nombre, apellido, telefono, correo, contrasenna)
        # Añadimos el objeto a la lista enlazada
        lista_enlazada_usuarios.add(nuevo_usuario)

    def menu_administrador(self):
        print("menu administrador")

