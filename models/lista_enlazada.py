from models.nodo import Nodo
from models.usuarios import Usuario

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

    def editar_usuario(self, correo):
        actual = self.head
        index = 1
        while actual is not None:
            if actual.dato.correo == correo:
                # Pide los nuevos datos
                rol = input(f"Ingrese el rol [{actual.dato.rol}]: ") or actual.dato.rol
                nombre = input(f"Ingrese el nombre [{actual.dato.nombre}]: ") or actual.dato.nombre
                apellido = input(f"Ingrese el apellido [{actual.dato.apellido}]: ") or actual.dato.apellido
                telefono = input(f"Ingrese el telefono [{actual.dato.telefono}]: ") or actual.dato.telefono
                correo = input(f"Ingrese el correo [{actual.dato.correo}]: ") or actual.dato.correo
                contrasenna = input(f"Ingrese el contraseña [{actual.dato.contrasenna}]: ") or actual.dato.contrasenna

                # Los asigna de una vez al nodo
                actual.dato.rol = rol
                actual.dato.nombre = nombre
                actual.dato.apellido = apellido
                actual.dato.telefono = telefono
                actual.dato.correo = correo
                actual.dato.contrasenna = contrasenna

                # Mandamos un objeto a modificar xml, junto a su index
                usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasenna)
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
        
        