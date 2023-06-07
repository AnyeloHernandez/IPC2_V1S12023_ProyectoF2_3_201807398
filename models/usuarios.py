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