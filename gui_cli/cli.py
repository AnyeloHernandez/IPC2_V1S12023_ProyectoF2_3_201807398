from models.carga_xml import *
import time

lista_enlazada_usuarios = cargar_usuarios_xml()
lista_doble_enlazada_salas = cargar_salas_xml()
lista_doble_circular_peliculas = cargar_peliculas_xml()

class Cli:
    global marco
    marco = "*" * 30

    def __init__(self):
        while True:
            self.menu_inicio()

    def menu_inicio_sesion(self):
        correo = input("Ingrese su correo: ")
        contrasenna = input("Ingrese su contraseña: ")
        # lista_enlazada_usuarios.imprimir_lista()
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
        while True:
            print(marco)
            print("1. Ver listado de peliculas")
            print("2. Peliculas favoritas")
            print("3. Comprar boletos")
            print("4. Historial de boletos comprados")
            print("5. Cerrar sesión")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Ve listado de peliculas
                self.menu_ver_peliculas()
            elif opcion == "2": # Ve listado de peliculas favoritas
                self.menu_peliculas_favoritas()
            elif opcion == "3": # Compra boletos
                self.menu_comprar_boletos()
            elif opcion == "4": # Historial de boletos
                lista_enlazada_usuarios.historial_boletos_comprados()
            elif opcion == "5":
                print("Se ha cerrado sesión...")
                break
            else:
                print("Ingrese una opción válida.")

    def menu_peliculas_favoritas(self):
        while True:
            print(marco)
            print("1. Añadir pelicula a favoritos")
            print("2. Eliminar pelicula de favoritos")
            print("3. Ver peliculas favoritas")
            print("4. Regresar al menu anterior")
            print(marco)
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                titulo = input("Ingrese el titulo de la pelicula: ")
                try:
                    buscar, categoria = lista_doble_circular_peliculas.buscar_pelicula(titulo)
                    if buscar == 1:
                        lista_enlazada_usuarios.insertar_peliculas_favoritas(categoria)
                except:
                    print("No se ha encontrado la pelicula")
            elif opcion == "2":
                titulo = input("Ingrese el titulo de la pelicula: ")
                lista_enlazada_usuarios.eliminar_peliculas_favoritas(titulo)
            elif opcion == "3":
                lista_enlazada_usuarios.imprimir_peliculas_favoritas()
            elif opcion == "4":
                break
            else:
                print("Ingrese una opción válida.")


    def menu_comprar_boletos(self):
        opcion = input("Ingrese el nombre de la pelicula que desea ver: ")
        try:
            buscar, categoria = lista_doble_circular_peliculas.buscar_pelicula(opcion)
            if buscar == 1:
                print(marco)
                print(f"Ha selecciónado la pelicula {categoria.pelicula.titulo}")
                print(f"Fecha de proyección: {categoria.pelicula.fecha} {categoria.pelicula.hora}")
                cantidad = int(input("Ingrese la cantidad de boletos que desea comprar: "))
                sala_seleccionada = int(input("Ingrese el número de sala: "))
                compra = lista_doble_enlazada_salas.buscar_sala(sala_seleccionada, cantidad)
                if compra:
                    self.menu_facturacion(cantidad, compra, categoria)
        except:
            print("No se ha encontrado la pelicula.")

    def menu_facturacion(self, cantidad, compra, categoria):
        print(marco)
        print("Ingrese los datos de facturación: ")
        nombre = input("Ingrese su nombre [CF]: ") or "CF"
        if nombre == "CF":
            self.imprimir_factura(cantidad, compra, categoria)
        else:
            nit = int(input("Ingrese su nit: "))
            direccion = input("Ingrese su dirección: ")
            self.imprimir_factura(cantidad, compra, categoria, nombre, nit, direccion)

    def imprimir_factura(self, cantidad, compra, categoria, nombre="Consumidor Final", nit="CF", direccion="Ciudad"):
        fecha = time.asctime()
        factura = f"""
            Documento Tributario Electronico
                      ORIGINAL
            --------------------------------
                    USAC Cinema
Universidad de San Carlos de Guatemala, zona 12, Facultad de Ingeniería
            --------------------------------
                --DATOS DEL COMPRADOR--
            Fecha de emisión {fecha}
            Nombre: {nombre}
            Nit: {nit}
            Dirección: {direccion}
            --------------------------------
             --DESCRIPCION DE LA FACTURA--
            Cine:
            Cine ABC
            Película:
            {categoria.pelicula.titulo}
            Sala:
            #USACIPC2_201807398_{compra.numero}
            Asientos:
            {cantidad}

            Total: Q.{cantidad * 32}
            """
        print(factura)
        lista_enlazada_usuarios.insertar_boletos_comprados(cantidad, nombre, nit, direccion, fecha, categoria)

    def menu_registrar(self, rol='cliente'):
        try:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = int(input("Ingrese su número de teléfono: ")) # Revisar si se puede con str o int
            correo = input("Ingrese su correo: ")
            contrasenna = input("Ingrese su contraseña: ")
            # Instanciamos un nuevo usuario
            nuevo_usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasenna)
            # Lo cargamos en el XML
            nuevo_usuario_xml(nombre, apellido, telefono, correo, contrasenna)
            # Añadimos el objeto a la lista enlazada
            lista_enlazada_usuarios.add(nuevo_usuario)
        except ValueError:
            print("Ingrese un número de teléfono válido")
        

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
                self.menu_administrador_gestionar_peliculas()
            elif opcion == "3": # Gestiona salas
                self.menu_administrador_gestionar_salas()
            elif opcion == "4": # Gestiona boletos comprados
                pass
            elif opcion == "5":
                print("Se ha cerrado sesión...")
                break
            else:
                print("Ingrese una opción válida.")

    def menu_administrador_gestionar_peliculas(self):
        while True:
            print(marco)
            print("1. Nueva categoria/pelicula")
            print("2. Editar categoria/pelicula")
            print("3. Eliminar categoria/pelicula")
            print("4. Ver peliculas disponibles")
            print("5. Salir del menu gestionar peliculas")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Crear peliculas/categoria
                self.admin_crear_peliculas()
            elif opcion == "2": # Editar peliculas
                self.admin_editar_peliculas()
            elif opcion == "3": # Eliminar peliculas
                self.admin_eliminar_peliculas()
            elif opcion == "4": # Ver peliculas
                self.menu_ver_peliculas()
            elif opcion == "5":
                print("Se ha regresado al menu principal de administrador")
                break
            else:
                print("Ingrese una opción válida.")

    def admin_editar_peliculas(self):
        try:
            titulo = input("Ingrese el titulo de la pelicula que desea editar: ")
            cate, index = lista_doble_circular_peliculas.editar_peliculas(titulo)
            modificar_pelicula_xml(cate, index)
        except:
            print("Ocurrio un error.")
    
    def admin_eliminar_peliculas(self):
        titulo = input("Ingrese el titulo de la pelicula que desea eliminar: ")
        pelicula_eliminada = lista_doble_circular_peliculas.delete(titulo)
        if pelicula_eliminada == 1:
            eliminar_pelicula_xml(titulo)
            print("Se eliminó la pelicula.")

    def menu_ver_peliculas(self):
        while True:
            print(marco)
            print("1. Ver por categoria")
            print("2. Ver listado general")
            print("3. Salir del menu ver peliculas")
            print(marco)
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                categoria = input("Ingrese la categoria: ")
                print(marco)
                print(f"+++Peliculas de {categoria}+++")
                lista_doble_circular_peliculas.imprimir_lista(opcion, categoria)
                print(marco)
            elif opcion == "2":
                lista_doble_circular_peliculas.imprimir_lista(opcion, None)
            elif opcion == "3":
                break
            else:
                print("Ingrese una opción válida.")

    def admin_crear_peliculas(self):
        while True:
            print(marco)
            print("1. Crear categoria")
            print("2. Añadir pelicula")
            print("3. Cancelar")
            print(marco)

            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Crea una categoria
                nombre = input("Ingrese el nombre de la categoria nueva: ")
                while not nombre:
                    nombre = input("El nombre no puede estar vacio. Ingrese el nombre de la categoria nueva: ")
                if nombre:
                    nueva_categoria_xml(nombre)
                    break
                else:
                    print("Ingrese un valor correcto")
                
            elif opcion == "2": # Crea una pelicula
                categoria = input("Ingrese la categoria en la que añadira la pelicula: ")
                titulo = input("Ingrese el titulo de la pelicula: ")
                director = input("Ingrese el director de la pelicula: ")
                anno = input("Ingrese el año de la pelicula: ")
                fecha = input("Ingrese la fecha de proyección la pelicula: ")
                hora = input("Ingrese la hora de proyección de la pelicula: ")
                registro = nueva_pelicula_xml(categoria, titulo, director, anno, fecha, hora)
                if registro == 1:
                    pelicula = Pelicula(titulo, director, anno, fecha, hora)
                    cate = Categoria(categoria, pelicula)
                    lista_doble_circular_peliculas.add(cate)
                    break
                else:
                    print("Ocurrio un error(No se encontró la categoria).")
            elif opcion == "3": # Regresa al menu anterior
                break
            else:
                print("Ingrese una opción válida")

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
                self.admin_eliminar_usuarios()
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
        try:
            usuario, index = lista_enlazada_usuarios.editar_usuario(correo)
            modificar_usuarios_xml(usuario, index)
            print("Se ha editado el usuario.")
        except:
            print("Ocurrio un error. Se salió del modo edición.")

    def admin_eliminar_usuarios(self):
        correo = input("Ingrese el correo del usuario que quiere eliminar: ")
        usuario_eliminado = lista_enlazada_usuarios.delete(correo)
        if usuario_eliminado == 1:
            eliminar_usuario_xml(correo)
            print(f"Usuario {correo} eliminado.")
        else:
            print("No se encontró el usuario.")

    def menu_administrador_gestionar_salas(self):
        while True:
            print(marco)
            print("1. Habilitar una sala nueva")
            print("2. Editar salas existentes")
            print("3. Deshabilitar salas")
            print("4. Ver salas disponibles")
            print("5. Salir del menu gestionar salas")
            print(marco)
            opcion = input("Ingrese una opción: ")
            if opcion == "1": # Crea salas
                self.admin_crear_salas()
            elif opcion == "2": # Editar salas
                self.admin_editar_salas()
            elif opcion == "3": # Eliminar salas
                self.admin_eliminar_salas()
            elif opcion == "4": # Ver salas
                lista_doble_enlazada_salas.imprimir_lista()
            elif opcion == "5":
                print("Se ha regresado al menu principal de administrador")
                break
            else:
                print("Ingrese una opción válida.")

    def admin_crear_salas(self):
        numero = int(input("Ingrese el nuevo número de sala: #USACIPC2_201807398_"))
        asientos = int(input("Ingrese el número de asientos: "))
        nueva_sala = Sala(numero, asientos)
        nueva_sala_xml(nueva_sala)

        numero = '#USACIPC2_201807398_' + str(numero)
        nueva_sala = Sala(numero, asientos)
        lista_doble_enlazada_salas.add(nueva_sala)

    def admin_editar_salas(self):
        try:
            numero_sala = int(input("Ingrese el número de sala que desea editar: "))
            sala_editada, index = lista_doble_enlazada_salas.editar_sala(numero_sala)
            modificar_sala_xml(sala_editada, index)
            print(f"Se modifico la sala #USACIPC2_201807398_{numero_sala}")
        except:
            print("Ocurrio un error. Se salió del modo edición.")

    def admin_eliminar_salas(self):
        try:
            numero_sala = int(input("Ingrese el número de sala que desea elminar: "))
            sala_eliminada = lista_doble_enlazada_salas.delete(numero_sala)
            # lista_doble_enlazada_salas.imprimir_lista()
            if sala_eliminada == 1:
                eliminar_sala_xml(numero_sala)
                print(f"Sala #USACIPC2_201807398_{numero_sala} eliminada.")
        except ValueError:
            print("Ingrese un valor valido")