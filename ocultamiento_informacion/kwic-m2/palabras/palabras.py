"""
Modulo que arma las lineas del texto en una estructura para ser manipulada posteriormente
"""


class Palabras:
    """
    Lista de palabras, pueder ser una oración, un renglon, una linea
    """
    def __init__(self):
        """
        Se inicializa como lista
        """
        self._lista_de_palabras = []

    def agregar_palabra(self, palabra):
        if (palabra is None) or (palabra == ''):
            raise Exception("Error: se quiso agregar una palabra vacía")
        self._lista_de_palabras.append(palabra)

    def obtener_palabra(self, posicion):
        if self._existe_posicion_palabra(posicion):
            return self._lista_de_palabras[posicion]
        else:
            raise Exception("No existe la posición de la palabra")

    def obtener_cadena_de_palabras(self):
        return self._lista_de_palabras

    def obtener_cantidad_de_palabras(self):
        return len(self._lista_de_palabras)

    def _existe_posicion_palabra(self, posicion):
        return True if posicion <= len(self._lista_de_palabras) else False


class Lineas:
    """
    Lista de lineas de un texto, pueden ser conjunto de renglones o de oraciones
    """
    def __init__(self):
        """
        Se inicializa como una lista de lineas de trxto
        """
        self._lista_del_lineas = []

    def obtener_lineas(self):
        return self._lista_del_lineas

    def agregar_linea(self, palabras):
        if palabras is None:
            raise Exception("Error: no hay palabras para agregar")
        self._lista_del_lineas.append(palabras)

    def obtener_linea(self, numero_de_linea):
        """
        Recupera la linea numerada
        """
        if self._existe_numero_de_linea(numero_de_linea):
            return self._lista_del_lineas[numero_de_linea]
        else:
            raise Exception('No existe el numero de linea')

    def obtener_palabra(self, numero_de_linea, posicion_de_palabra):
        """
        Recupera la palabra de la posicion en la linea
        """
        if self._existe_numero_de_linea(numero_de_linea):
            linea = self._lista_del_lineas[numero_de_linea]
            return linea.obtener_palabra(posicion_de_palabra)
        else:
            raise Exception('No existe el numero de linea')

    def _existe_numero_de_linea(self, numero_de_linea):
        return True if numero_de_linea <= len(self._lista_del_lineas) else False
