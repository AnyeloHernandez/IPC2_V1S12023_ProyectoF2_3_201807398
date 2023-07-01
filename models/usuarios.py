class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contrasenna):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasenna = contrasenna

    def imprimir_usuarios(self):
        print(f"Nombre: {self.nombre} {self.apellido}\nTelefono: {self.telefono}\nCorreo: {self.correo}")
        print("")

class Boleto():
    def __init__(self, numero_sala, numero_boleto, cantidad, nombre, nit, direccion, correo, fecha, pelicula, total):
        self.numero_sala = numero_sala
        self.numero_boleto = numero_boleto
        self.total = total
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.cantidad = cantidad
        self.correo = correo
        self.fecha = fecha
        self.pelicula = pelicula