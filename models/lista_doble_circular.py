from models.nodo import Nodo
from models.peliculas import Pelicula, Categoria

class ListaDobleCircular:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.actual = self.head
        return self
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration  
        data = self.actual.dato  
        self.actual = self.actual.siguiente
        if self.actual == self.head:
            self.actual = None 
        return data

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

        if actual is None:
            return print("La lista esta vacia")
        
        while True:
            if actual.dato.pelicula.titulo == titulo:
                if actual.siguiente == actual:
                    self.head = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                    if actual == self.head:
                        self.head = actual.siguiente
                return 1
            actual = actual.siguiente
            if actual == self.head:
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

    def editar_peliculas(
            self, categoria, titulo, titulo_editado, director, imagen, anno, fecha, hora):
        actual = self.head
        index = 1
        temp = actual.dato.nombre

        if actual is None:
            return None

        while True:
            print(actual.dato.nombre)
            if actual.dato.pelicula.titulo == titulo:
                #pide los datos nuevos
                # categoria = input(f"Ingrese la categoria [{actual.dato.nombre}]: ") or actual.dato.nombre
                
                # actual.dato.nombre = categoria
                # actual.dato.categoria.titulo = titulo
                # actual.dato.categoria.direcor = director
                # actual.dato.categoria.imagen = imagen
                # actual.dato.categoria.anno = anno
                # actual.dato.categoria.fecha = fecha
                # actual.dato.categoria.hora = hora

                pelicula = Pelicula(titulo, director, imagen, anno, fecha, hora)                
                cate = Categoria(actual.dato.nombre, pelicula)
                
                return cate, index
            if actual.dato.nombre != temp:
                index = 1
            else:
                index += 1
            actual = actual.siguiente
            if actual == self.head:
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