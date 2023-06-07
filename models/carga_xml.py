import xml.etree.ElementTree as ET
from models.usuarios import Usuario
from models.lista_enlazada import *

def cargar_usuarios_xml():
    tree = ET.parse('db/usuarios.xml')
    root = tree.getroot()
    listaenlazada = ListaEnlazada()

    for usuario in root.findall('usuario'):
        rol = usuario.find('rol').text
        nombre = usuario.find('nombre').text
        apellido = usuario.find('apellido').text
        telefono = usuario.find('telefono').text
        correo = usuario.find('correo').text
        contrasenna = usuario.find('contrasena').text

        objeto = Usuario(rol, nombre, apellido, telefono, correo, contrasenna) #Instanciamos el objeto
        
        listaenlazada.add(objeto)
    return listaenlazada
        #print(f"nombre: {nombre} {apellido}, telefono: {telefono}, correo {correo}")

