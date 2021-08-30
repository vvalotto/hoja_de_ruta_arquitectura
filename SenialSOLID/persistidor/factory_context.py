from .contexto import *


class FactoryContexto(object):
    """
    Responsable de crear la clase de contexto de datos
    """

    @staticmethod
    def obtener_contexto(tipo_contexto, param):

        contexto = None
        if tipo_contexto == 'archivo':
            contexto = ContextoArchivo(param)

        elif tipo_contexto == 'pickle':
            contexto = ContextoPickle(param)

        return contexto