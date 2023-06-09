from models.carga_xml import *

lista_enlazada_usuarios = cargar_usuarios_xml()


class Cli:
    global marco
    marco = "*" * 30

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

    def menu_inicio(self):
        print(marco)
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        print(marco)

        opcion = input("Ingrese opción: ")
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
        while True:
            print(marco)
            print("1. Ver listado de peliculas")
            print("2. Ver listado de peliculas favoritas")
            print("3. Comprar boletos")
            print("4. Historial de boletos comprados")
            print("5. Cerrar sesión")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Ve listado de peliculas
                pass
            elif opcion == "2": # Ve listado de peliculas favoritas
                pass
            elif opcion == "3": # Compra boletos
                pass
            elif opcion == "4": # Historial de boletos
                pass
            elif opcion == "5":
                print("Se ha cerrado sesión...")
                break
            else:
                print("Ingrese una opción válida.")

    def menu_registrar(self, rol='cliente'):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = int(input("Ingrese su número de telefono: ")) # Revisar si se puede con str o int
        correo = input("Ingrese su correo: ")
        contrasenna = input("Ingrese su contraseña: ")
        # Instanciamos un nuevo usuario
        nuevo_usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasenna)
        # Lo cargamos en el XML
        nuevo_usuario_xml(nombre, apellido, telefono, correo, contrasenna)
        # Añadimos el objeto a la lista enlazada
        lista_enlazada_usuarios.add(nuevo_usuario)

    def menu_administrador(self):
        print("+++Bienvenido al menu de administrador super secreto+++")
        while True:
            print(marco)
            print("1. Gestionar usuarios")
            print("2. Gestionar categorías y peliculas")
            print("3. Gestionar salas")
            print("4. Gestionar boletos comprados")
            print("5. Salir del menu administrador")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Gestiona usuarios
                self.menu_administrador_gestionar_usuarios()
            elif opcion == "2": # Gestiona peliculas
                pass
            elif opcion == "3": # Gestiona salas
                pass
            elif opcion == "4": # Gestiona boletos comprados
                pass
            elif opcion == "5":
                print("Se ha cerrado sesión...")
                break
            else:
                print("Ingrese una opción válida.")

    def menu_administrador_gestionar_usuarios(self):
        while True:
            print(marco)
            print("1. Crear usuario nuevo")
            print("2. Editar usuarios")
            print("3. Eliminar usuarios")
            print("4. Ver usuarios existentes")
            print("5. Salir del menu gestionar usuarios")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Crea usuarios
                self.admin_crear_usuarios()
            elif opcion == "2": # Editar usuario
                self.admin_editar_usuarios()
            elif opcion == "3": # Eliminar usuarios
                pass
            elif opcion == "4": # Ver usuarios
                lista_enlazada_usuarios.imprimir_lista()
            elif opcion == "5":
                print("Se ha regresado al menu principal de administrador")
                break
            else:
                print("Ingrese una opción válida.")

    def admin_crear_usuarios(self):
        while True:
            print(marco)
            print("Ingrese que tipo de usuario quiere crear.")
            print("1. Cliente")
            print("2. Administrador")
            print("3. Salir del menu")
            print(marco)
            opcion = input("Ingrese una opcion")
            if opcion == "1":
                self.menu_registrar()
                break
            elif opcion == "2":
                self.menu_registrar("administrador")
                break
            elif opcion == "3":
                break
            else:
                print("Seleccione una opción válida.")

    def admin_editar_usuarios(self):
        correo = input("Ingrese el correo del usuario que quiere editar: ")
        usuario, index = lista_enlazada_usuarios.editar_usuario(correo)
        modificar_xml(usuario, index)
        print("Se ha editado el usuario.")