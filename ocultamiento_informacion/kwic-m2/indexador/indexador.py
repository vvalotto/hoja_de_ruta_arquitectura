"""
Módulo de extrae los indices (posiciones) de las palabras clave de cada linea de texto
"""


class Indexador:
    """
    Crea y trata los indices de la palabras clave de una linea de texto
    """
    PALABRAS_EXCLUIDAS = ['LA', 'LAS', 'EL', 'LOS', 'DE', 'DEL', 'A', 'O',
                          'PARA', 'POR', 'QUE', 'SE', 'SI', 'Y', 'SU'
                          ]

    def __init__(self, lineas):
        self._lineas = lineas
        self._palabras_indices = []

    def generar_indices_de_palabras(self):

        for linea in self._lineas.obtener_lineas():
            indices_por_linea = []
            for palabra in linea.obtener_cadena_de_palabras():
                if palabra not in self.PALABRAS_EXCLUIDAS:
                    indices_por_linea.append(linea.obtener_cadena_de_palabras().index(palabra))
            self._palabras_indices.append(indices_por_linea)

    def obtener_indices_de_palabras(self):
        return self._palabras_indices
