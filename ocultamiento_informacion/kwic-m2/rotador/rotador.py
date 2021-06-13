"""
Modulo que arma una lista cadenas circulares de palabras, una por cada linea de texto leida.
Cada una de las cadenas solo contiene la palabras con significado (Palabras claves)
"""


class Rotador:

    def __init__(self, lineas):
        """
        Constructor del rotador.
        Se instancia con la lineas que deben ser transformadas en
        cadenas de palabras circulares
        """
        self._lineas = lineas
        self._lineas_circulares = []  # Lista de cadenas circulares

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
            # Inicializa posicion de las palabras de la lista a tratar
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
        """
        linea_circular = ""
        linea_circular_original = self._lineas_circulares[numero_linea]
        paso = 0
        while paso < linea_circular_original.obtener_tamanio():
            celda = linea_circular_original.obtener_celda(puntero)
            palabra = celda.obtener_contenido()
            puntero = celda.obtener_proxima_celda()
            linea_circular = linea_circular + palabra + " "
            paso += 1
        return linea_circular


class Celda:
    """
    Componente de una lista circular
    """
    def __init__(self, contenido, proxima_celda):
        """
        Crea elemento
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
        """
        self._cadena.append(celda)

    def obtener_celda(self, posicion):
        """
        Recupera una celda de acuerdo a la posición en la lista
        """
        return self._cadena[posicion]

    def obtener_cadena(self):
        """
        Devuelva la lista circular de celdas
        """
        return self._cadena

    def obtener_tamanio(self):
        """
        Devuelve la cantidad de elementos de la lista
        """
        return len(self._cadena)
