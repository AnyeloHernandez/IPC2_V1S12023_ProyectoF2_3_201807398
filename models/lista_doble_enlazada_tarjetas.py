from models.nodo import Nodo
from models.usuarios import Tarjeta

class ListaDobleEnlazadaTarjetas():
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

    def __iter__(self):
        actual = self.head

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
            
    def imprimir_lista(self):
        if self.isEmpty() is False:
            actual = self.head
            actual.dato.imprimir_tarjetas()
            while actual.siguiente is not None:
                actual = actual.siguiente
                actual.dato.imprimir_tarjetas()
        else:
            print("La lista esta vacia")

    def delete(self, numero):
        actual = self.head
        
        while actual is not None:
            print(actual.dato.numero)
            print(numero)
            if numero == actual.dato.numero:
                if actual.anterior is None:
                    self.head = actual.siguiente
                    if self.head:
                        self.head.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior
                return 1
            actual = actual.siguiente
        else:
            print("No se encontró la tarjeta.")

    def isEmpty(self): # Revisa si la lista esta vacia
        if self.head is None:
            return True
        return False