"""
Modulo que arma las lineas del texto en una estructura para ser manipulada posteriormente
"""


class Palabras:
    """
    Conjunto de palabras, pueder ser una oración, un renglon, una linea
    """
    def __init__(self):
        """
        Se inicializa como lista
        """
        self._lista_de_palabras = []

    def agregar_palabra(self, palabra):
        self._lista_de_palabras.append(palabra)

    def obtener_palabra(self, posicion):
        return self._lista_de_palabras[posicion]

    def obtener_cadena_de_palabras(self):
        return self._lista_de_palabras

    def obtener_cantidad_de_palabras(self):
        return len(self._lista_de_palabras)


class Lineas:
    """
    Conjunto de lineas de un texto, pueden ser conjunto de renglones o de oraciones
    """
    def __init__(self):
        """
        Se inicializa como una lista de lineas de trxto
        """
        self._lista_del_lineas = []

    def obtener_lineas(self):
        return self._lista_del_lineas

    def agregar_linea(self, palabras):
        self._lista_del_lineas.append(palabras)

    def obtener_linea(self, numero_de_linea):
        """
        Recupera la linea numerada
        :param numero_de_linea:
        :return:
        """
        return self._lista_del_lineas[numero_de_linea]

    def obtener_palabra(self, numero_de_linea, posicion_de_palabra):
        """
        Recupera la palabra de la posicion en la linea
        :param numero_de_linea:
        :param posicion_de_palabra:
        :return:
        """
        return self._lista_del_lineas[numero_de_linea].obtener_palabra[posicion_de_palabra]
