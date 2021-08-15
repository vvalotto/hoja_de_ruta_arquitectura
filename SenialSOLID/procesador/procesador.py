"""
Para OCP
Se refactoriza la clase de manera de extender otros tipos de
funciones de adquisicion de datos sin que impacte en los anteriores programas
o que cambiando solo las clases de alto nivel que puedan "armar" la solucion

Se modifica el constructor, se le inyecta es tipo de señal definida para
la adquisicion
"""
from abc import ABCMeta, abstractmethod


class BaseProcesador(metaclass=ABCMeta):
    """
    Clase Abstracta Procesador
    """
    def __init__(self, senial):
        """
        Se inicializa con la senial que se va a procesar
        """
        self._senial_procesada = senial
        return

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
    def __init__(self, senial, amplificacion):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el valor de amplificacion
        :param senial:
        :param amplificacion:
        :return:
        """
        BaseProcesador.__init__(self, senial)
        self._amplificacion = amplificacion

    def procesar(self, senial):
        """
        Implementa el procesamiento de amplificar cada valor de senial
        :param senial:
        :return:
        """
        print("Procesando...")
        self._senial_procesada.valores = list(map(self._amplificar, senial.valores))
        self._senial_procesada.cantidad += len(self._senial_procesada.valores)
        return

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
    def __init__(self, senial, umbral):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el umbral
        :param umbral:
        :return:
        """
        BaseProcesador.__init__(self, senial)
        self._umbral = umbral

    def procesar(self, senial):
        """
        Implementa el procesamiento de la senial con umbral
        :param senial:
        :return:
        """
        print("Procesando con umbral")
        self._senial_procesada.valores = list(map(self._funcion_umbral, senial.valores))
        self._senial_procesada.cantidad += len(self._senial_procesada.valores)
        return

    def _funcion_umbral(self, valor):
        """
        Funcion que filtra valores con un umbral
        :param valor:
        :return:
        """
        return valor if valor < self._umbral else 0
