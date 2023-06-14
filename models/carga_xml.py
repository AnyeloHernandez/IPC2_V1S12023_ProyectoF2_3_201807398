import xml.etree.ElementTree as ET
from models.usuarios import Usuario
from models.salas import Sala
from models.peliculas import Pelicula, Categoria
from models.lista_enlazada import ListaEnlazada
from models.lista_doble_enlazada import ListaDobleEnlazada
from models.lista_doble_circular import ListaDobleCircular

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

def eliminar_pelicula_xml(titulo):
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()

    for categoria in root.findall('categoria'):
        peliculas = categoria.find('peliculas')

        for pelicula in peliculas.findall('pelicula'):
            if titulo == pelicula.find('titulo').text:
                peliculas.remove(pelicula)
                tree.write('db/peliculas.xml')
        

def modificar_pelicula_xml(cate, index):
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()

    for categoria in root.findall('categoria'):
        nombre_categoria = categoria.find('nombre').text
        
        if cate.nombre == nombre_categoria:
            print("Se encontro la categoria")
            peliculas = categoria.find('peliculas')

            titulo = peliculas.find(f'pelicula[{index}]/titulo')
            director = peliculas.find(f'pelicula[{index}]/director')
            anno = peliculas.find(f'pelicula[{index}]/anio')
            fecha = peliculas.find(f'pelicula[{index}]/fecha')
            hora = peliculas.find(f'pelicula[{index}]/hora')

            # Editamos el XML
            titulo.text = cate.pelicula.titulo
            director.text = cate.pelicula.director
            anno.text = cate.pelicula.anno
            fecha.text = cate.pelicula.fecha
            hora.text = cate.pelicula.hora

            # Lo escribimos en el XML
            tree.write('db/peliculas.xml')


def cargar_peliculas_xml():
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()
    #categorias = root.find('categoria')
    listadoblecircular = ListaDobleCircular()
    
    #print(categoria.findall('nombre'))

    for categoria in root.findall('categoria'):
       # print(f"Peliculas de {categoria.find('nombre').text}")
       nombre_categoria = categoria.find('nombre').text
       for pelicula in categoria.findall(f'peliculas/pelicula'):
           titulo = pelicula.find('titulo').text
           director = pelicula.find('director').text
           anno = pelicula.find('anio').text
           fecha = pelicula.find('fecha').text
           hora = pelicula.find('hora').text
           peli = Pelicula(titulo, director, anno, fecha, hora)
           cate = Categoria(nombre_categoria, peli)
           #print(cate.nombre)
           #print(cate.pelicula.titulo)
           listadoblecircular.add(cate)
    return listadoblecircular

def nueva_categoria_xml(nombre):
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()
    
    datos_categoria = f"""
        <categoria>
        <nombre>{nombre}</nombre>
        <peliculas>
        </peliculas>
        </categoria>
        """
    categoria = ET.fromstring(datos_categoria)
    root.append(categoria)
    tree.write('db/peliculas.xml')

def nueva_pelicula_xml(categoria, titulo, director, anno, fecha, hora):
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()

    datos_pelicula = f"""
    <pelicula>
    <titulo>{titulo}</titulo>
    <director>{director}</director>
    <anio>{anno}</anio>
    <fecha>{fecha}</fecha>
    <hora>{hora}</hora>
    </pelicula>
        """
    
    for item in root.findall('categoria'):
        if categoria == item.find('nombre').text:
            pelicula = item.find('peliculas')
            nueva_pelicula = ET.fromstring(datos_pelicula)
            pelicula.append(nueva_pelicula)
            tree.write('db/peliculas.xml')
            print(f"Se añadió la pelicula correctamente a la categoria {categoria}")
            return 1
    
def buscar_categoria(categoria):
    tree = ET.parse('db/peliculas.xml')
    root = tree.getroot()
    #categorias = root.find('categoria')
    index = 1
    #print(categoria.findall('nombre'))

    for item in root.findall('categoria'):
        if categoria == item.find('nombre').text:
            break
        else:
            index += 1
    return index

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
    salas = cine.find('salas')
    salas.append(sala)

    tree.write('db/salas.xml')
    print("Se ha habilitado la sala correctamente.")

def eliminar_sala_xml(numero_sala):
    sala_eliminada = "#USACIPC2_201807398_" + str(numero_sala)
    tree = ET.parse('db/salas.xml')
    root = tree.getroot()

    cine = root.find('cine')
    salas = cine.find('salas') # Busca las salas en el cine en este orden debido al xml root>cine>salas

    # Busca la sala y si la encuentra la elimina
    for sala in salas.findall('sala'):
        if sala.find('numero').text == sala_eliminada:
            salas.remove(sala)
            tree.write('db/salas.xml')
            break

def modificar_sala_xml(sala_editada, index):
    tree = ET.parse('db/salas.xml')
    root = tree.getroot()
    cine = root.find('cine')
    salas = cine.find('salas')

    numero_sala = salas.find(f"sala[{index}]/numero")
    asientos = salas.find(f"sala[{index}]/asientos")
    
    # Edita el XML para las salas
    numero_sala.text = '#USACIPC2_201807398_' + sala_editada.numero
    asientos.text = sala_editada.asientos

    tree.write('db/salas.xml')