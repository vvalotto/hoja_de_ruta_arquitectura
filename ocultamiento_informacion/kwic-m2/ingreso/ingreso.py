"""
Modulo que lee el archivo de texto y lo convierta en una
estructura de lineas interna
"""
from palabras.palabras import *


def leer_linea_texto(nombre_archivo):
    lineas = Lineas()
    try:
        archivo = open(nombre_archivo, 'r')
        lineas_leidas = archivo.readlines()
        archivo.close()
    except IOError:
        print("Error en la lectura del archivo")
    else:
        for linea in lineas_leidas:
            palabras = Palabras()
            for palabra in linea.split():
                palabras.agregar_palabra(palabra)
            lineas.agregar_linea(palabras)
    return lineas
