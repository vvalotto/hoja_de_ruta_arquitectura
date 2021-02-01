"""


"""


def crear_lista_palabras_indices(cadena_de_palabras, indices_por_linea):
    """

    :param cadena_de_palabras:
    :param indices_por_linea:
    :return:
    """
    numero_de_linea = 0
    lista_palabras_indices = []
    for indices in indices_por_linea:
        for indice in indices:
            celda_a_ordenar = [cadena_de_palabras[numero_de_linea][indice], numero_de_linea, indice]
            lista_palabras_indices.append(celda_a_ordenar)
        numero_de_linea += 1

    return lista_palabras_indices


def ordenar_palabras(cadena_de_palabras, indices_por_linea):
    """

    :param cadena_de_palabras:
    :param indices_por_linea:
    :return:
    """
    lista_ordenada = crear_lista_palabras_indices(cadena_de_palabras, indices_por_linea)

    for puntero_a in range(0, len(lista_ordenada)):
        for puntero_b in range(puntero_a + 1, len(lista_ordenada)):
            if lista_ordenada[puntero_a][0][0] > lista_ordenada[puntero_b][0][0]:
                elemento_seleccionado = lista_ordenada[puntero_b]
                lista_ordenada[puntero_b] = lista_ordenada[puntero_a]
                lista_ordenada[puntero_a] = elemento_seleccionado
    return lista_ordenada
