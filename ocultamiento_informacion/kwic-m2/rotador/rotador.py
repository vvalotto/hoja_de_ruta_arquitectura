"""

"""


class Rotador:

    PALABRAS_EXCLUIDAS = ['LA', 'LAS', 'EL', 'LOS', 'DE', 'DEL', 'A', 'O', 'PARA', 'POR', 'QUE', 'SE', 'SI', 'Y']

    def __init__(self, lineas):
        """
        Constructor del rotados.
        Se instancia con la lineas que deben ser transformadas en
        cadenas de palabras circulares
        :param lineas: conjunto de lineas de texto
        """
        self._lineas = lineas
        self._lineas_circulares = []  # Lista de cadenas circulares
        self._palabras_indices = []

    def obtener_linea(self, numero_de_linea):
        return self._lineas.obtener_linea(numero_de_linea)

    def armar_cadenas_circulares(self):
        """
        Transforma las lineas de texto ingresadas en cadenas de celda de palabras
        circulares
        """
        for linea in self._lineas.obtener_lineas():
            """
            Para cada linea genera una cadena circular
            """
            cadena = CadenaCircular()
            # Inicializa posicion de las palabras de la lista a trata
            posicion = 1
            for palabra in linea.obtener_cadena_de_palabras():
                """
                Para cada palabra de la lista, pasa la palabra a la celda de la
                cadena circular
                """
                cadena.agregar_celda(Celda(palabra, posicion))
                posicion += 1
                if posicion == linea.obtener_cantidad_de_palabras():
                    posicion = 0
            self._lineas_circulares.append(cadena)

    def obtener_cantidad_lineas(self):
        return len(self._lineas_circulares)

    def obtener_linea_rotada(self, numero_linea, puntero):
        """
        Devuelve la cadena de caracteres compuesta de la cadena de palabras
        que esta en el renglon (numero de linea) y empieza por la palabra apuntada
        por puntero
        :param numero_linea:
        :param puntero:
        :return:
        """
        linea_circular = ""
        linea_circular_original = self._lineas_circulares[numero_linea]
        for iterador in range(0, linea_circular_original.obtener_tamanio()):
            celda = linea_circular_original.obtener_celda(puntero)
            palabra = celda.obtener_contenido()
            puntero = celda.obtener_proxima_celda()
            linea_circular = linea_circular + palabra + " "
        return linea_circular

    def generar_indices_de_palabras(self):

        for linea in self._lineas.obtener_lineas():
            indices_por_linea = []
            for palabra in linea.obtener_cadena_de_palabras():
                if palabra not in self.PALABRAS_EXCLUIDAS:
                    indices_por_linea.append(linea.obtener_cadena_de_palabras().index(palabra))
            self._palabras_indices.append(indices_por_linea)

    def obtener_indices_de_palabras(self):
        return self._palabras_indices


class Celda:
    """
    Componente de una lista circular
    """
    def __init__(self, contenido, proxima_celda):
        """
        Crea elemento
        :param contenido: 
        :param proxima_celda: 
        """
        self._contenido = contenido
        self._proxima_celda = proxima_celda

    def obtener_contenido(self):
        return self._contenido

    def obtener_proxima_celda(self):
        return self._proxima_celda

    def __str__(self):
        return self._contenido


class CadenaCircular:
    """
    Estructura: cadena circular de elementos.
    Es una lista de celdas, donde cada celda tiene un contenido y la posicion de la
    próxima celda
    """
    def __init__(self):
        """
        Se crea la estrucrtura vacía
        """
        self._cadena = []  # lista de celdas

    def agregar_celda(self, celda):
        """
        Se agrega una celda a la cadena al final de la lista
        :param celda:
        :return:
        """
        self._cadena.append(celda)

    def obtener_celda(self, posicion):
        """
        Recupera una celda de acuerdo a la posición en la lista
        :param posicion: posición de la celda en la lista
        :return:
        """
        return self._cadena[posicion]

    def obtener_cadena(self):
        """
        Devuelva la lista circular de celdas
        :return:
        """
        return self._cadena

    def obtener_tamanio(self):
        """
        Devuelve la cantidad de elementos de la lista
        :return:
        """
        return len(self._cadena)
