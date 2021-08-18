"""
Modulo que contiene la responsabilidad de guardar las seniales, adquiridas y procesadas
en algun tipo de almacen de persistencia (archivo plano, xml, serializa, base de dato)
"""
import os
import pickle


class PersistidorPickle(object):
    """
    Clase de persistidor que persiste un tipo de objeto de manera serializada
    """
    def __init__(self, recurso):
        """
        Se crea el archivo con el path donde se guardarán los archivos
        de la entidades a persistir
        :param recurso: Path del repositorio de entidades
        :return:
        """
        try:
            self.__recurso = recurso
            if not os.path.isdir(recurso):
                os.mkdir(recurso)
        except IOError as eIO:
            raise eIO

    def persistir(self, entidad, nombre_entidad):
        """
        Se persiste el objeto (entidad) y se indica el tipo de entidad
        :param: entidad (object)
        :param: nombre_entidad (string)
        """
        archivo = str(nombre_entidad) + '.pickle'
        ubicacion = self.__recurso + "/" + archivo
        try:
            with open(ubicacion, "wb") as a:
                pickle.dump(entidad, a)
        except IOError as eIO:
            raise eIO
        return

    def recuperar(self, id_entidad):
        """
        Se lee el entidad a tratar
        :param id_entidad
        :return: entidad (object)
        """
        archivo = str(id_entidad) + '.pickle'
        ubicacion = self.__recurso + "/" + archivo
        e = None
        try:
            with open(ubicacion, "rb") as a:
                e = pickle.load(a)
        except IOError as eIO:
            print(eIO)
        except ValueError as eVE:
            print(eVE)
        return e
