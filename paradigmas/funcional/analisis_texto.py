"""
Ejemplo para el paradigma de programación declarativa - Programación Funcional
"""

CARACTERES_DESCARTABLES = [',', '.', ':', ';', '-', '_']


def filtrar_caracteres_alfabeticos(texto):

    return ''.join(list(filter(lambda caracter: caracter not in CARACTERES_DESCARTABLES, texto)))


def depurar_texto(texto):

    return filtrar_caracteres_alfabeticos(texto).lower()


def obtener_palabras(texto):

    return depurar_texto(texto).split()


def contar_palabras(texto):

    return len(obtener_palabras(texto))


def obtener_palabras_iniciadas_con(texto, letra):

    return list(filter(lambda palabra: palabra[0] == letra, obtener_palabras(texto)))


def contar_palabras_iniciadas_con(texto, letra):

    return len(obtener_palabras_iniciadas_con(texto, letra))
