class Pelicula:
    def __init__(self, titulo, director, anno, fecha, hora):
        self.titulo = titulo
        self.director = director
        self.anno = anno
        self.fecha = fecha
        self.hora = hora

    def imprimir_peliculas(self):
        print(f"Titulo: {self.titulo}\nDirector(es): {self.director}\nAño: {self.anno}\nFecha y hora: {self.hora} {self.fecha}")
        print("")