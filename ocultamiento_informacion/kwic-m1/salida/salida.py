"""
Módulo que arma las frases en contexto para cada palabra clave y muestra el resultado
"""


def armar_frase_con_contexto(palabra_en_contexto, linea):
    """
    Genera la frase completa comenzando con la palabra clave provista en palabra_en_contexto
    """
    frase = []
    contexto = linea[palabra_en_contexto[2]]
    frase.append(contexto[0])

    largo_linea = len(linea) - 1
    paso = 0
    while paso < largo_linea:
        contexto = linea[contexto[1]]
        frase.append(contexto[0])
        paso += 1
    return frase


def armar_kwic(cadena_de_palabras, lista_ordenada):
    """
    Genera la lista completa de líneas de frases en contexto
    """
    palabras_clave_en_contexto = []
    for elemento in lista_ordenada:
        palabras_clave_en_contexto.append(
            armar_frase_con_contexto(elemento, cadena_de_palabras[elemento[1]]))

    return palabras_clave_en_contexto


def mostrar_kwic(cadena_de_palabras, lista_ordenada):
    """
    Muestra por consola la lista de frase en contexto
    """
    palabras_clave_en_contexto = armar_kwic(cadena_de_palabras, lista_ordenada)
    for linea in palabras_clave_en_contexto:
        frase = ''
        for palabra in linea:
            frase = frase + palabra + ' '
        print(frase)
