"""
Módulo que arma las frases en contexto para cada palabra clave y muestra el resultado
"""


def armar_frase_con_contexto(palabra_en_contexto, linea):
    """
    ToDo: Falta Descripción
    """
    frase = []
    contexto = linea[palabra_en_contexto[2]]
    frase.append(contexto[0])
    for puntero in range(0, len(linea) - 1):
        contexto = linea[contexto[1]]
        frase.append(contexto[0])
    return frase


def armar_indices_en_contexto(cadena_de_palabras, lista_ordenada):
    """
    ToDo: Falta Descripción
    """
    palabras_clave_en_contexto = []
    for elemento in lista_ordenada:
        palabras_clave_en_contexto.append(
            armar_frase_con_contexto(elemento, cadena_de_palabras[elemento[1]]))

    return palabras_clave_en_contexto


def mostrar_kwic(cadena_de_palabras, lista_ordenada):
    """
    ToDo: Falta Descripción
    """
    palabras_clave_en_contexto = armar_indices_en_contexto(cadena_de_palabras, lista_ordenada)
    for linea in palabras_clave_en_contexto:
        frase = ''
        for palabra in linea:
            frase = frase + palabra + ' '
        print(frase)
