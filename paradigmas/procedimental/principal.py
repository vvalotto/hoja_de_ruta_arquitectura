from procedimental.analisis_texto import *

texto = 'No son las cosas que nos pasan las que nos hacen sufrir, sino lo que nosotros nos decimos sobre esas cosas'
print(' ')
print('Las palabras del texto son:')
print(obtener_palabras(texto))
print(' ')
print('Hay {} palabras'.format(contar_palabras(texto)))

letra_inicial = 's'
print(' ')
print('Las palabras del texto que comienzan con {} son:'.format(letra_inicial))
print(obtener_palabras_iniciadas_con(texto, letra_inicial))
print(' ')
print('Hay {} palabras'.format(contar_palabras_iniciadas_con(texto, letra_inicial)))
