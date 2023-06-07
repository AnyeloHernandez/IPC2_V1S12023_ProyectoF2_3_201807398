from gui_cli.cli import Cli
from models.usuarios import Usuario
from models.carga_xml import cargar_usuarios_xml
from models.lista_enlazada import *

if __name__ == '__main__':
    print("Cargando...")
    # Para trabajar el xml en todos lados:
    # lista_enlazada_usuarios = cargar_usuarios_xml()
    # lista_enlazada_usuarios.imprimir_lista()
    Cli()