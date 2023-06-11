import xml.etree.ElementTree as ET
from models.usuarios import Usuario
from models.salas import Sala
from models.lista_enlazada import ListaEnlazada
from models.lista_doble_enlazada import ListaDobleEnlazada

def cargar_usuarios_xml():
    tree = ET.parse('db/usuarios.xml')
    root = tree.getroot()
    listaenlazada = ListaEnlazada()
    # print(root)
    for usuario in root.findall('usuario'):
        rol = usuario.find('rol').text
        nombre = usuario.find('nombre').text
        apellido = usuario.find('apellido').text
        telefono = usuario.find('telefono').text
        correo = usuario.find('correo').text
        contrasenna = usuario.find('contrasena').text

        usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasenna) #Instanciamos el objeto
        # Lo añadimos a la Lista Enlazada
        listaenlazada.add(usuario)
        # print(f"nombre: {nombre} {apellido}, telefono: {telefono}, correo {correo}")
    return listaenlazada
        

def nuevo_usuario_xml(nombre, apellido, telefono: int, correo, contrasenna):
    tree = ET.parse('db/usuarios.xml')
    root = tree.getroot()

    # Añadimos el usuario
    datos_usuario = f'''
    <usuario>
    <rol>cliente</rol>
    <nombre>{nombre}</nombre>
    <apellido>{apellido}</apellido>
    <telefono>{telefono}</telefono>
    <correo>{correo}</correo>
    <contrasena>{contrasenna}</contrasena>
    </usuario>
        '''
    # print(texto)
    usuario = ET.fromstring(datos_usuario)
    root.append(usuario)

    # Escribe en el XML
    tree.write('db/usuarios.xml')
    print("Se añadio el usuario correctamente.")

def modificar_usuarios_xml(usuario_editado, index):
    tree = ET.parse('db/usuarios.xml')
    root = tree.getroot()
    
    rol = root.find(f"usuario[{index}]/rol")
    nombre = root.find(f"usuario[{index}]/nombre") # etiqueta con indice y etiqueta hija, en i debe ir el indice
    apellido = root.find(f"usuario[{index}]/apellido")
    telefono = root.find(f"usuario[{index}]/telefono")
    correo = root.find(f"usuario[{index}]/correo")
    contrasenna = root.find(f"usuario[{index}]/contrasena")
    
    # Edita el XML
    rol.text = usuario_editado.rol
    nombre.text = usuario_editado.nombre
    apellido.text = usuario_editado.apellido
    telefono.text = usuario_editado.telefono
    correo.text = usuario_editado.correo
    contrasenna.text = usuario_editado.contrasenna

    # Escribe los cambios en el XML
    tree.write("db/usuarios.xml")

def eliminar_usuario_xml(correo):
    tree = ET.parse('db/usuarios.xml')
    root = tree.getroot()

    for usuario in root.findall('usuario'):
        if usuario.find('correo').text == correo:
            root.remove(usuario)
            tree.write('db/usuarios.xml')
            break

def cargar_peliculas_xml():
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()
    pass

def cargar_salas_xml():
    tree = ET.parse('db/salas.xml')
    root = tree.getroot()
    listadobleenlazada = ListaDobleEnlazada()
    cine = root.find('cine')

    for sala in cine.findall('salas/sala'):
        numero = sala.find('numero').text
        asientos = sala.find('asientos').text
        nueva_sala = Sala(numero, asientos)
        listadobleenlazada.add(nueva_sala)
        # print(f"Numero de sala: {numero} Asientos: {asientos}")
    return listadobleenlazada

def nueva_sala_xml(sala):
    tree = ET.parse('db/salas.xml')
    root = tree.getroot()
    
    datos_sala = f"""
    <sala>
    <numero>#USACIPC2_201807398_{sala.numero}</numero>
    <asientos>{sala.asientos}</asientos>
    </sala>
    """

    sala = ET.fromstring(datos_sala)
    cine = root.find('cine')
    cine.append(sala)

    tree.write('db/salas.xml')
    print("Se ha habilitado la sala correctamente.")