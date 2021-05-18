"""
Ejemplo para el paradigma de programación imperativa - Programación Procedimiental y modular
"""

CARACTERES_DESCARTABLES = [',', '.', ':', ';', '-', '_']


def filtrar_caracteres_alfabeticos(texto):
    """
    Elimina los caracteres que no son alfabeticos en el texto
    :param texto: texto a analizar
    :return: Texto sin caracteres especiales o de puntuación
    """
    texto_filtrado = ''
    for caracter in texto:
        if caracter not in CARACTERES_DESCARTABLES:
            texto_filtrado += caracter

    return texto_filtrado


def depurar_texto(texto):
    """
    Pasa las palabras del texto a minuscula
    :param texto: texto solo con palabras a analizar
    :return: texto sin minúscula
    """
    texto_con_palabras = filtrar_caracteres_alfabeticos(texto)
    texto_con_palabras_en_minusculas = texto_con_palabras.lower()

    return texto_con_palabras_en_minusculas


def obtener_palabras(texto):
    """
    Genera un lista de palabras desde un texto
    :param texto: texto orginal a analizar
    :return: lista de palabras
    """
    texto_depurado = depurar_texto(texto)
    lista_de_palabras = texto_depurado.split()

    return lista_de_palabras


def contar_palabras(texto):
    """
    Cuenta las palabras de un texto
    :param texto: texto orginal a analizar
    :return: Cantidad de palabras
    """
    return len(obtener_palabras(texto))


def obtener_palabras_iniciadas_con(texto, letra):
    """
    Obtiene una lista de palabras que empiezan con una letra definida
    :param texto: texto orginal a analizar
    :param letra: letra que se quiere buscar en cada palabra del texto
    :return: lista de palabras
    """
    lista_de_palabras = []
    for palabra in obtener_palabras(texto):
        if palabra[0] == letra:
            lista_de_palabras.append(palabra)

    return lista_de_palabras


def contar_palabras_iniciadas_con(texto, letra):
    """
    Cuenta la cantidad de palabras de un texto que empiezan con la letra definida
    :param texto: texto orginal a analizar
    :param letra: letra que se quiere buscar en cada palabra del texto
    :return: cantidad de palabras encontradas
    """
    return len(obtener_palabras_iniciadas_con(texto, letra))


def contar_palabra_en_texto(texto, palabra_a_buscar):
    """
    Obtiene la cantidad de veces que aparace la palabra definida
    :param texto: texto orginal a analizar
    :param palabra_a_buscar:
    :return: cantidad de apariciones de la palabra buscada
    """
    conteo = 0
    for palabra in obtener_palabras(texto):
        if palabra_a_buscar == palabra:
            conteo += 1
    return conteo
