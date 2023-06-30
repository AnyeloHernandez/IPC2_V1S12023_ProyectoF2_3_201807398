from models.nodo import Nodo
from models.usuarios import Usuario, Boleto

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.boletos_comprados = []
        self.peliculas_favoritas = []
        self.usuario_logeado = ""
        self.rol_logeado = ""

    def __iter__(self):
        self.actual = self.head
        return self
    
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            data = self.actual.dato
            self.actual = self.actual.siguiente
            return data

    def add(self, dato):
        nuevo = Nodo(dato)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def imprimir_lista(self):
        actual = self.head
        actual.dato.imprimir_usuarios()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir_usuarios()

    def login(self, correo, contrasenna):
        actual = self.head

        while actual is not None: # Si el nodo actual no es None ejecuta
            if actual.dato.correo == correo and actual.dato.contrasenna == contrasenna:
                if actual.dato.rol == "administrador":
                    self.rol_logeado = "administrador"
                    self.usuario_logeado = actual.dato.correo
                    # Muestra el menu de administrador
                    # print("Se ingreso como administrador")
                    return 1
                elif actual.dato.rol == "cliente":
                    # Muestra el menu de cliente
                    self.usuario_logeado = actual.dato.correo
                    print(f"Bienvenido: {actual.dato.nombre} {actual.dato.apellido}")
                    return 2
                else:
                    print("Correo o contraseña incorrectos.")
                    return False
            actual = actual.siguiente # Avanza el nodo y repite

    def editar_usuario(self, correo, correo_editado, rol, nombre, apellido, telefono, contrasenna):
        actual = self.head
        index = 1
        while actual is not None:
            if actual.dato.correo == correo:

                # Los asigna de una vez al nodo
                actual.dato.rol = rol
                actual.dato.nombre = nombre
                actual.dato.apellido = apellido
                actual.dato.telefono = telefono
                actual.dato.correo = correo_editado
                actual.dato.contrasenna = contrasenna

                # Mandamos un objeto a modificar xml, junto a su index
                usuario = Usuario(rol, nombre, apellido, telefono, correo_editado, contrasenna)
                return usuario, index
            index += 1
            
            actual = actual.siguiente

    def delete(self, correo):
        actual = self.head
        anterior = None

        while actual is not None:
            if actual.dato.correo == correo:
                if anterior is None:
                    self.head = actual.siguiente
                    return 1
                else:
                    anterior.siguiente = actual.siguiente
                    return 1
            anterior = actual
            actual = actual.siguiente

    def insertar_boletos_comprados(self, numero_boleto, cantidad, nombre, nit, direccion, fecha, pelicula, total):
        correo = self.usuario_logeado
        boleto = Boleto(numero_boleto, cantidad, nombre, nit, direccion, correo, fecha, pelicula, total)
        boletos_comprados = self.boletos_comprados
        boletos_comprados.append(boleto)

    def historial_boletos_comprados(self):
        boletos_comprados = self.boletos_comprados
        print(f"Historial de {self.usuario_logeado}: \n")
        for boleto in boletos_comprados:
            if boleto.correo == self.usuario_logeado:
                print(f"Titulo de la pelicula: {boleto.pelicula.pelicula.titulo}")
                print(f"Fecha de compra: {boleto.fecha}")
                print(f"Asientos comprados: {boleto.cantidad}")
                print(f"Nombre: {boleto.nombre}")
                print(f"NIT: {boleto.nit}")
                print(f"Direccón: {boleto.direccion}")
                print(f"Total: {boleto.total}")
                print("")

    def insertar_peliculas_favoritas(self, categoria):
        peliculas_favoritas = self.peliculas_favoritas
        favorita = (categoria, self.usuario_logeado)
        if favorita not in peliculas_favoritas:
            peliculas_favoritas.append(favorita)
            print(f"Se ha añadido la pelicula {categoria.pelicula.titulo} a sus favoritos")
        else:
            print("La pelicula ya está en sus favoritos.")

    def imprimir_peliculas_favoritas(self):
        peliculas_favoritas = self.peliculas_favoritas
        print(f"Peliculas favoritas:\n")
        for pelicula, usuario in peliculas_favoritas:
            if usuario == self.usuario_logeado:
                print(f"Titulo: {pelicula.pelicula.titulo}")
                print(f"Director(es): {pelicula.pelicula.director}")
                print(f"Género: {pelicula.nombre}")
                print(f"Año: {pelicula.pelicula.anno}")
                print("")

    def eliminar_peliculas_favoritas(self, titulo):
        peliculas_favoritas = self.peliculas_favoritas
        print(self.usuario_logeado)
        for pelicula, usuario in peliculas_favoritas:
            if usuario == self.usuario_logeado and titulo == pelicula.pelicula.titulo:
                peliculas_favoritas.remove((pelicula, usuario))
                print(f"Se ha eliminado la pelicula {pelicula.pelicula.titulo}")