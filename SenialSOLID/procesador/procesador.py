"""
Para OCP
Se refactoriza la clase de manera de extender otros tipos de
funciones de procesmiento de datos sin que impacte en los anteriores programas
o que cambiando solo las clases de alto nivel que pueda "armar" la solucion
"""
from abc import ABCMeta, abstractmethod
from SenialSOLID.modelo.senial import *


class BaseProcesador(metaclass=ABCMeta):
    """
    Clase Abstracta Procesador
    """
    def __init__(self):
        """
        Se inicializa con la senial que se va a procesar
        """
        self._senial_procesada = Senial()

    @abstractmethod
    def procesar(self, senial):
        """
        Método abstracto que se implementara para cada tipo de procesamiento
        """
        pass

    def obtener_senial_procesada(self):
        """
        Devuelve la señal procesada
        """
        return self._senial_procesada


class ProcesadorAmplificador(BaseProcesador):
    """
    Clase Procesador Amplificador
    """
    def __init__(self, amplificacion):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el valor de amplificacion
        """
        BaseProcesador.__init__(self)
        self._amplificacion = amplificacion

    def procesar(self, senial):
        """
        Implementa el procesamiento de amplificar cada valor de senial
        """
        print("Procesando...")
        self._senial_procesada.valores = list(map(self._amplificar, senial.valores))
        self._senial_procesada.tamanio = senial.tamanio

    def _amplificar(self, valor):
        """
        Funcion que retorna el doble de valor de entrada
        :param valor:
        :return:
        """
        return valor * self._amplificacion


class ProcesadorConUmbral(BaseProcesador):
    """
    Clase Procesador con Umbral
    """
    def __init__(self, umbral):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el umbral
        :param umbral:
        :return:
        """
        BaseProcesador.__init__(self)
        self._umbral = umbral

    def procesar(self, senial):
        """
        Implementa el procesamiento de la senial con umbral
        :param senial:
        :return:
        """
        print("Procesando con umbral")
        self._senial_procesada._valores = list(map(self._funcion_umbral, senial._valores))

    def _funcion_umbral(self, valor):
        """
        Funcion que filtra valores con un umbral
        :param valor:
        :return:
        """
        return valor if valor < self._umbral else 0
