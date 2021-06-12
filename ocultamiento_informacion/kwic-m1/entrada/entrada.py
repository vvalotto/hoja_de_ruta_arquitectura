"""
El modulo de entrada lee las lineas desde un medio de almacenamiento (un archivo por ejemplo y lo guarda en
en estructura para procesamiento posterior. En este caso lo almacenará en un arreglo circular de caracteres, donde
cada elemento del arreglo es la palabra y la posición de la próxima palabra.
"""


def leer_linea_texto(nombre_archivo):
    lista_lineas = []  # lista de lineas o renglones del texto de entrada
    try:
        archivo = open(nombre_archivo, 'r')
        lineas = archivo.readlines()
        archivo.close()
    except IOError:
        print("Error en la lectura del archivo")
    else:
        for linea in lineas:
            posicio_proxima_palabra = 1
            palabras_en_la_linea = []

            for palabra in linea.split():
                palabras_en_la_linea.append([palabra, posicio_proxima_palabra])
                posicio_proxima_palabra += 1

                if posicio_proxima_palabra == len(linea.split()):
                    posicio_proxima_palabra = 0
            lista_lineas.append(palabras_en_la_linea)
    return lista_lineas
