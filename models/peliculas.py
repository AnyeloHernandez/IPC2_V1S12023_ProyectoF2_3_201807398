class Pelicula:
    def __init__(self, titulo, director, anno, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anno = anno
        self.fecha = fecha
        self.hora = hora

class Categoria(Pelicula):
    def __init__(self, nombre, pelicula):
        self.nombre = nombre
        self.pelicula = pelicula

    def imprimir_peliculas_general(self):
        print(f"Categoria: {self.nombre}")
        print(f"Titulo: {self.pelicula.titulo}\nDirector(es):"+
              f"{self.pelicula.director}\nAño: {self.pelicula.anno}"+
              f"\nFecha y hora: {self.pelicula.hora} {self.pelicula.fecha}")
        print("")

    def imprimir_peliculas_categoria(self, categoria):
        if categoria == self.nombre:
            print(f"Titulo: {self.pelicula.titulo}\nDirector(es):" +
                  f"{self.pelicula.director}\nAño: {self.pelicula.anno}" +
                  f"\nFecha y hora: {self.pelicula.hora} {self.pelicula.fecha}")
            print("")