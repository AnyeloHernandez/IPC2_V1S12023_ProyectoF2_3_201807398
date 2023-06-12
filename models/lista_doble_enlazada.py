from models.nodo import Nodo
from models.salas import Sala

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
        if self.isEmpty() is False:
            actual = self.head
            actual.dato.imprimir_salas()
            while actual.siguiente is not None:
                actual = actual.siguiente
                actual.dato.imprimir_salas()
        else:
            print("La lista esta vacia")

    def delete(self, sala):
        actual = self.head

        while actual is not None:
            if actual.dato.numero == ("#USACIPC2_201807398_" + str(sala)):
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
            print("No se encontró la sala.")

    def editar_sala(self, numero):
        actual = self.head
        index = 1

        while actual is not None:
            if actual.dato.numero == ("#USACIPC2_201807398_" + str(numero)):
                # Pide los datos
                numero = input(f"Ingrese la sala [{actual.dato.numero}]: #USACIPC2_201807398_") or actual.dato.numero
                asientos = input(f"Ingrese el número de asientos [{actual.dato.asientos}]: ") or actual.dato.asientos

                # Los asigna al nodo
                actual.dato.numero = "#USACIPC2_201807398_" + numero
                actual.dato.asientos = asientos

                # Mandamos el objeto a modificar
                sala = Sala(numero, asientos)
                return sala, index
            index += 1
            actual = actual.siguiente
            
    def isEmpty(self): # Revisa si la lista esta vacia
        if self.head is None:
            return True
        return False