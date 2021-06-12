"""
Módulo que genera las lista de palabras circulares e indices a las palabras claves de cada lista de palabras
"""
PALABRAS_EXCLUIDAS = ['LA', 'LAS', 'EL', 'LOS', 'DE', 'DEL']


def generar_indices_de_palabras(linea):
    """
    Se genera un lista de las posiciones de las palabras en la linea de texto, pero las lista de las posiciones
    son de aquellas palabras que pasan el filtro de palabras excluidas (articulos, conjunciones, preposiciones)
    """
    indices = []
    for palabra in linea:
        if palabra[0] not in PALABRAS_EXCLUIDAS:
            indices.append(linea.index(palabra))
    return indices


def armar_lineas_circulares(linea, indices):
    """
    ToDo: Descripción de la función
    """
    linea_circular = []
    for indice in indices:
        puntero = indice
        for contador_palabra in range(0, len(linea)):
            linea_circular.append(linea[puntero][0])
            puntero = linea[puntero][1]

    return linea_circular


def generar_indices_por_linea(cadena_de_palabras):
    """
    Genera un listado de índices (posiciones de palabras) por cada línea del texto ingresado en cadena de palabras
    llama a la función que genera el listado de indices de una línea
    """
    indices_por_linea = []
    for linea in cadena_de_palabras:
        indices_por_linea.append(generar_indices_de_palabras(linea))
    return indices_por_linea
