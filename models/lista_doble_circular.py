from models.nodo import Nodo
from models.peliculas import Pelicula, Categoria

class ListaDobleCircular:
    def __init__(self):
        self.head = None

    def add(self, dato):
        nodo = Nodo(dato)

        if self.head is None:
            nodo.siguiente = nodo
            nodo.anterior = nodo
            self.head = nodo
        else:
            ultimo = self.head.anterior

            nodo.siguiente = self.head
            nodo.anterior = ultimo

            self.head.anterior = nodo
            ultimo.siguiente = nodo

    def delete(self, titulo):
        actual = self.head
        temp = self.head
        while actual is not None:
            if actual.dato.pelicula.titulo == titulo:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                return 1
            actual = actual.siguiente
            if actual == temp:
                return print("No se encontro la pelicula.")
                

    def imprimir_lista(self, opcion, categoria):
        if self.head is not None:
            nodo = self.head
            while True:
                if opcion == "1":
                    nodo.dato.imprimir_peliculas_categoria(categoria)
                    nodo = nodo.siguiente
                elif opcion == "2":
                    nodo.dato.imprimir_peliculas_general()
                    nodo = nodo.siguiente

                if nodo == self.head:
                    break
        else:
            print("La lista esta vacia.")

    def editar_peliculas(self, titulo):
        actual = self.head
        temp = self.head
        index = 1
        while actual is not None:
            if actual.dato.pelicula.titulo == titulo:
                #pide los datos nuevos
                # categoria = input(f"Ingrese la categoria [{actual.dato.nombre}]: ") or actual.dato.nombre
                titulo = input(f"Ingrese el titulo [{actual.dato.pelicula.titulo}]: ") or actual.dato.pelicula.titulo
                director = input(f"Ingrese el director [{actual.dato.pelicula.director}]: ") or actual.dato.pelicula.director
                anno = input(f"Ingrese el año [{actual.dato.pelicula.anno}]: ") or actual.dato.pelicula.anno
                fecha = input(f"Ingrese la fecha [{actual.dato.pelicula.fecha}]: ") or actual.dato.pelicula.fecha
                hora = input(f"Ingrese la hora [{actual.dato.pelicula.hora}]: ") or actual.dato.pelicula.hora
                pelicula = Pelicula(titulo, director, anno, fecha, hora)
                cate = Categoria(actual.dato.nombre , pelicula)
                return cate, index
            index += 1
            actual = actual.siguiente
            if actual == temp:
                break

    def buscar_pelicula(self, titulo):
        actual = self.head
        temp = self.head
        index = 1

        while actual is not None:
            # Revisa que la pelicula exista
            if actual.dato.pelicula.titulo == titulo:
                return 1, actual.dato
            actual = actual.siguiente
            if actual == temp:
                break