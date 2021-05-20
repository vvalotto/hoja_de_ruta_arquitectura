"""
Ejemplo para el paradigma de programación declarativa - Programación Funcional
"""

CARACTERES_DESCARTABLES = [',', '.', ':', ';', '-', '_']


def filtrar_caracteres_alfabeticos(texto):
    """
    Elimina los caracteres que no son alfabeticos en el texto
    :param texto: texto a analizar
    :return: Texto sin caracteres especiales o de puntuación
    """
    return ''.join(list(filter(lambda caracter: caracter not in CARACTERES_DESCARTABLES, texto)))


def depurar_texto(texto):
    """
    Pasa las palabras del texto a minuscula
    :param texto: texto solo con palabras a analizar
    :return: texto sin minúscula
    """
    return filtrar_caracteres_alfabeticos(texto).lower()


def obtener_palabras(texto):
    """
    Genera un lista de palabras desde un texto
    :param texto: texto orginal a analizar
    :return: lista de palabras
    """
    return depurar_texto(texto).split()


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
    return list(filter(lambda palabra: palabra[0] == letra, obtener_palabras(texto)))


def contar_palabras_iniciadas_con(texto, letra):
    """
    Cuenta la cantidad de palabras de un texto que empiezan con la letra definida
    :param texto: texto orginal a analizar
    :param letra: letra que se quiere buscar en cada palabra del texto
    :return: cantidad de palabras encontradas
    """
    return len(obtener_palabras_iniciadas_con(texto, letra))
