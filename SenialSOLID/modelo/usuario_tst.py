__author__ = 'voval'
__project__ = ''

from .usuario import *
from SenialSOLID.persistidor.contexto import *
from SenialSOLID.persistidor.repositorio import *


def crear_usuario():
    usu = Usuario()
    nom = Nombre()
    nom.nombre = 'Victor'
    nom.apellido = 'Valotto'
    usu.id = 14367849
    usu.usuario = 'vvalotto'
    usu.clave = 'voval062'
    usu.nombre_apellido = str(nom)
    return usu


if __name__ == '__main__':
    contexto = ContextoArchivo('.')
    repo = RepositorioUsuario(contexto)
    usu = crear_usuario()
    repo.guardar(usu)
    print(usu.usuario)
    usu1 = repo.obtener(Usuario(), usu.id)
    print(usu1)
    print(usu1.usuario)
