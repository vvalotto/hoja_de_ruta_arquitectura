

def filtrar_caracteres_alfabeticos(texto):

    caracteres_descartables = [',', '.', ':', ';', '-', '_']
    return ''.join([caracter for caracter in texto if caracter not in caracteres_descartables])


def depurar_texto(texto):

    return filtrar_caracteres_alfabeticos(texto).lower()


def obtener_palabras(texto):

    return depurar_texto(texto).split()


def contar_palabras(texto):

    return len(obtener_palabras(texto))


def obtener_palabras_iniciadas_con(texto, letra):

    return [palabra for palabra in obtener_palabras(texto) if palabra[0] == letra]


def contar_palabras_iniciadas_con(texto, letra):

    return len(obtener_palabras_iniciadas_con(texto, letra))
