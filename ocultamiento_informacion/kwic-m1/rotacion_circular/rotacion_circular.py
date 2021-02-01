
PALABRAS_EXCLUIDAS = ['LA', 'LAS', 'EL', 'LOS', 'DE', 'DEL']


def generar_indices_de_palabras(linea):
    """

    :param linea:
    :return:
    """
    indices = []
    for palabra in linea:
        if palabra[0] not in PALABRAS_EXCLUIDAS:
            indices.append(linea.index(palabra))
    return indices


def armar_lineas_circulares(linea, indices):
    """

    :param linea:
    :param indices:
    :return:
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

    :param cadena_de_palabras:
    :return:
    """
    indices_por_linea = []
    for linea in cadena_de_palabras:
        indices_por_linea.append(generar_indices_de_palabras(linea))
    return indices_por_linea
