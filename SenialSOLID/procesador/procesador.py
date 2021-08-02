from SenialSOLID.modelo.senial import Senial


class Procesador:
    """
    Define la clase procesador de la senial
    """

    def __init__(self, parametro):
        """
        Constructor: Inicializa la senial que resultara procesada.
        """
        self._senial_procesada = Senial()
        self._parametro = parametro
    
    def procesar_senial(self, senial):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :return:
        """
        print("Procesando...")
        self._senial_procesada._valores = list(map(self.funcion_doble, senial._valores))

    def procesar_senial_con_umbral(self, senial):
        """
        Metodo que realiza el procesamiento de la senial con umbral
        :param senial: a procesar
        :return:
        """
        print("Procesando con umbral")
        self._senial_procesada._valores = list(map(self.funcion_umbral, senial._valores))

    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada

    def funcion_doble(self, valor):
        """
        Funcion que retorna el doble de valor de entrada
        :param valor:
        :return:
        """
        return valor * self._parametro

    def funcion_umbral(self, valor):
        """
        Funcion que filtra valores con un umbral
        :param valor:
        :return:
        """
        return valor if valor < self._parametro else 0
