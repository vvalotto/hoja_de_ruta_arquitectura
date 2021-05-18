"""
Programa principal que la clase definida para analizar el texto. Programación Orientada a Objetos
"""

from objetos.analizador_texto import *

mi_texto = 'No son las cosas que nos pasan las que nos hacen sufrir, sino lo que nosotros nos decimos sobre esas cosas'
analizador = AnalizadorTexto(mi_texto)

print(' ')
print('Las palabras del texto son:')
print(analizador.obtener_palabras())
print(' ')
print('Hay {} palabras'.format(analizador.contar_palabras()))

letra_inicial = 's'
print(' ')
print('Las palabras del texto que comienzan con {} son:'.format(letra_inicial))
print(analizador.obtener_palabras_iniciadas_con(letra_inicial))
print(' ')
print('Hay {} palabras'.format(analizador.contar_palabras_iniciadas_con( letra_inicial)))

