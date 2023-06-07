from models.nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.head = None

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

        while actual is not None:
            if actual.dato.correo == correo and actual.dato.contrasenna == contrasenna:
                print("Inicio de sesion correcto")
            else:
                print("ocurrio un error")
            
            actual = actual.siguiente