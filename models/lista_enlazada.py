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

        while actual is not None: # Si el nodo actual no es None ejecuta
            if actual.dato.correo == correo and actual.dato.contrasenna == contrasenna:
                if actual.dato.rol == "administrador":
                    # Muestra el menu de administrador
                    # print("Se ingreso como administrador")
                    return 1
                elif actual.dato.rol == "cliente":
                    # Muestra el menu de cliente
                    print(f"Bienvenido: {actual.dato.nombre} {actual.dato.apellido}")
                    return 2
                else:
                    print("Correo o contraseña incorrectos.")
                    return False
            actual = actual.siguiente # Avanza el nodo y repite