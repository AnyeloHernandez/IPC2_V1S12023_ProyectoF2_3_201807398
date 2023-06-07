from models.carga_xml import cargar_usuarios_xml

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
        lista_enlazada_usuarios.login(correo, contrasenna)
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
        if opcion == "2": # Registrar usuario
            pass
        if opcion == "3": # Sale del sistema
            print("Se ha salido del sistema. Tenga un buen día.")
            exit()
        
    def menu_cliente(self):
        '''
        todo: 
        Ver listado de peliculas en general
        Listado de peliculas favoritas del usuario
        Comprar boletos para la pelicula
        Historial de boletos
        '''
        pass

    def menu_registrar(self):
        pass

