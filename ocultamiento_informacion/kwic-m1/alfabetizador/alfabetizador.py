"""
Módulo que ordena la palabras indices de cada frase de manera alfabética
"""


def crear_lista_palabras_indices(cadena_de_palabras, indices_por_linea):
    """
    Se arma una lista, donde cada elemento de la misma tiene:
    - la celda con la palabra clave
    - el numero de la linea del texto que contiene esa palabra
    - la posicion en la linea de esa palabra clave
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
    Genera un lista de palabra clave, ordenadas alfabeticamente por es palabra clave.
    Las lista esta compuesta de:
    - la celda con la palabra clave
    - el numero de la linea del texto que contiene esa palabra
    - la posicion en la linea de esa palabra clave
    """
    lista_ordenada = crear_lista_palabras_indices(cadena_de_palabras, indices_por_linea)

    for puntero_a in range(0, len(lista_ordenada)):
        for puntero_b in range(puntero_a + 1, len(lista_ordenada)):
            if lista_ordenada[puntero_a][0][0] > lista_ordenada[puntero_b][0][0]:
                elemento_seleccionado = lista_ordenada[puntero_b]
                lista_ordenada[puntero_b] = lista_ordenada[puntero_a]
                lista_ordenada[puntero_a] = elemento_seleccionado
    return lista_ordenada
