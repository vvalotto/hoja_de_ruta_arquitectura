"""
Modulo que contiene la responsabilidad de guardar las seniales, adquiridas y procesadas
en algun tipo de almacen de persistencia (archivo plano, xml, serializa, base de dato)
"""
import os
import pickle
from .mapeador import *


class Persistidor(metaclass=ABCMeta):
    """
    Clase abstract que define la interfaz de la persistencia de datos
    """
    def __init__(self, recurso):
        """
        Se crea el contexto, donde el nombre es el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico con el nombre
        :param recurso:
        :return:
        """
        if recurso is None or recurso == "":
            raise Exception("Nombre de recurso vacio")
        self._recurso = recurso

    @property
    def recurso(self):
        return self._recurso

    @abstractmethod
    def persistir(self, entidad, nombre_entidad):
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es el tipo a persistir
        """
        pass

    @abstractmethod
    def recuperar(self, id_entidad, entidad):
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es devuelta por el metodo
        """
        pass


class PersistidorPickle(Persistidor):
    """
    Clase de persistidor que persiste un tipo de objeto de manera serializada
    """
    def __init__(self, recurso):
        """
        Se crea el archivo con el path donde se guardaran los archivos
        de la entidades a persistir
        :param recurso: Path del repositorio de entidades
        :return:
        """
        try:
            super().__init__(recurso)
            self._recurso = recurso
            if not os.path.isdir(recurso):
                os.mkdir(recurso)
        except IOError as eIO:
            raise eIO

    def persistir(self, entidad, id_entidad):
        """
        Se persiste el objeto (entidad) y se indica el tipo de entidad
        :param: entidad (object)
        :param: id_entidad (string)
        """
        archivo = str(id_entidad) + '.pickle'
        ubicacion = self._recurso + "/" + archivo
        try:
            with open(ubicacion, "wb") as a:
                pickle.dump(entidad, a)
        except IOError as eIO:
            raise eIO

    def recuperar(self, entidad, id_entidad):
        """
        Se lee el entidad a tratar
        :param entidad
        :param id_entidad
        :return: entidad (object)
        """
        archivo = str(id_entidad) + '.pickle'
        ubicacion = self._recurso + "/" + archivo
        e = None
        try:
            with open(ubicacion, "rb") as a:
                e = pickle.load(a)
        except IOError as eIO:
            print(eIO)
        except ValueError as eVE:
            print(eVE)
        return e


class PersistidorArchivo(Persistidor):
    """
    Contexto del recurso de persistencia de tipo archivo
    """
    def __init__(self, recurso):
        """
        Se crea el archivo con el path donde se guardaran los archivos
        de la entidades a persistir
        :param recurso: Path del repositorio de entidades
        :return:
        """
        try:
            super().__init__(recurso)
            if not os.path.isdir(recurso):
                os.mkdir(recurso)
        except IOError as eIO:
            raise eIO

    def persistir(self, entidad, nombre_entidad):
        """
        Agregar un objeto(entidad) para persistirlo.
        :param entidad: Tipo de entidad
        :param nombre_entidad: identificacion de la instancia de la entidad
        :return:
        """
        mapeador = MapeadorArchivo()
        archivo = str(nombre_entidad) + '.dat'
        contenido = mapeador.ir_a_persistidor(entidad)
        ubicacion = self._recurso + "/" + archivo

        try:
            with open(ubicacion, "w") as a:
                a.write(contenido)
        except IOError as eIO:
            raise eIO

    def recuperar(self, entidad, id_entidad):
        """
        Obtiene la entidad guardada
        :param entidad:
        :param id_entidad:
        :return:
        """
        contenido = ''
        archivo = str(id_entidad) + '.dat'
        ubicacion = self._recurso + "/" + archivo
        try:
            with open(ubicacion) as persitidor:
                linea = persitidor.readline()
                while linea != '':
                    contenido = contenido + linea
                    linea = persitidor.readline()
            mapeador = MapeadorArchivo()
            return mapeador.venir_desde_persistidor(entidad, contenido)
        except IOError as eIO:
            raise eIO
        except ValueError:
            raise ValueError
