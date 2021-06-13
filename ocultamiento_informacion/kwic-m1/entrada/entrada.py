"""
El modulo de entrada lee las lineas desde un medio de almacenamiento (un archivo por ejemplo y lo guarda en
en estructura para procesamiento posterior. En este caso lo almacenará en un arreglo circular de caracteres, donde
cada elemento del arreglo es la palabra y la posición de la próxima palabra.
"""


def leer_texto(nombre_archivo):
    lineas =[]
    try:
        archivo = open(nombre_archivo, 'r')
        lineas = archivo.readlines()
        archivo.close()
    except IOError:
        print("Error en la lectura del archivo")
    return lineas

