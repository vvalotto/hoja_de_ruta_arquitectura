from entrada.entrada import *
from rotacion_circular.rotacion_circular import *
from alfabetizador.alfabetizador import *
from salida.salida import *


cadena_de_palabras = leer_linea_texto("texto.txt")
print('Cadena de palabras del texto')
print(cadena_de_palabras)
print('----------------------------')

indices_por_linea = generar_indices_por_linea(cadena_de_palabras)
print('Indice de las palabras del texto')
print(indices_por_linea)
print('---------------------------------')

lista_ordenada = ordenar_palabras(cadena_de_palabras, indices_por_linea)
print('Lista ordenada de la palabras clav2')
print(lista_ordenada)
print('---------------------------------')

print('Lista de KWIC')
mostrar_kwic(cadena_de_palabras, lista_ordenada)
print('---------------------------------')
