from models.nodo import Nodo

class ListaDobleEnlazada():
    def __init__(self):
        self.head = None

    def add(self, dato):
        nodo = Nodo(dato)

        if self.head is None:
            self.head = nodo
        else:
            actual = self.head

            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.anterior = actual
    
    def imprimir_lista(self):
        actual = self.head
        actual.dato.imprimir_salas()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir_salas()