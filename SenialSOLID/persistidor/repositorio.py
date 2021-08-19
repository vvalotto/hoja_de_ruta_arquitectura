"""
Patrón repositorio: responsable de manejar de manera abstracta la persitencia
de las entidades
"""
from abc import ABCMeta, abstractmethod


class BaseRepositorio(metaclass=ABCMeta):
    def _init__(self, contexto):
        self._contexto = contexto
    """
    Define la interfaz para el acceso a la persistencia de datos
    """
    @abstractmethod
    def guardar(self, entidad):
        """
        Persiste la entidad
        """
        pass

    @abstractmethod
    def obtener(self, entidad, id_entidad):
        pass


class RepositorioSenial(BaseRepositorio):

    def __init__(self, ctx):
        super()._init__(ctx)

    def guardar(self, senial):
        try:
            self._contexto.persistir(senial, senial.id)
        except Exception:
            raise Exception

    def obtener(self, senial, id_senial):
        try:
            return self._contexto.recuperar(senial, id_senial)
        except Exception:
            raise Exception
