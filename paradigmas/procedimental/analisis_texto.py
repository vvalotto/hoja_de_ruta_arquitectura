"""
Ejemplo para el paradigma de programación declarativo - Programación Procedimiental y modular
"""

CARACTERES_DESCARTABLES = [',', '.', ':', ';', '-', '_']


def filtrar_caracteres_alfabeticos(texto):
    """
    Elimina los caracteres que no son alfabeticos en el texto
    :param texto: texto a analizar
    :return: None
    """
    texto_filtrado = ''
    for caracter in texto:
        if caracter not in CARACTERES_DESCARTABLES:
            texto_filtrado += caracter

    return texto_filtrado


def depurar_texto(texto):

    texto_con_palabras = filtrar_caracteres_alfabeticos(texto)
    texto_con_palabras_en_minusculas = texto_con_palabras.lower()

    return texto_con_palabras_en_minusculas


def obtener_palabras(texto):
    texto_depurado = depurar_texto(texto)
    lista_de_palabras = texto_depurado.split()

    return lista_de_palabras


def contar_palabras(texto):
    return len(obtener_palabras(texto))


def obtener_palabras_iniciadas_con(texto, letra):
    lista_de_palabras = []
    for palabra in obtener_palabras(texto):
        if palabra[0] == letra:
            lista_de_palabras.append(palabra)
    return lista_de_palabras


def contar_palabras_iniciadas_con(texto, letra):
    return len(obtener_palabras_iniciadas_con(texto, letra))


def contar_palabra_en_texto(texto, palabra_a_buscar):
    conteo = 0
    for palabra in obtener_palabras(texto):
        if palabra_a_buscar == palabra:
            conteo += 1
    return conteo