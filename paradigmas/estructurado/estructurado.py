"""
Ejemplo para el paradigma de programación imperativa - Programación estructurada
"""

# Inicializacion de datos
print('INICIO')
TEXTO = 'Resistir y persistir. Entender con claridad, actuar con corrección y aceptar lo que fuera'
CARACTERES_DESCARTABLES = [',', '.', ':', ';', '-', '_']

# Bloque 1 - Depura el texto
texto_sin_puntuacion = ''
for caracter in TEXTO:
    if caracter not in CARACTERES_DESCARTABLES:
        texto_sin_puntuacion += caracter

print('Texto original: ' + TEXTO)
print('Texto con palabras: ' + texto_sin_puntuacion)
print('FIN - BLOQUE 1' + '\n')


# Bloque 2 - Cuenta palabras
texto_bajo_analisis = texto_sin_puntuacion.lower()
lista_de_palabras = texto_bajo_analisis.split()
print('Cantidad de palabras: {}'.format(len(lista_de_palabras)))
print('FIN - BLOQUE 2' + '\n')

# Bloque 3 - Cantidad de ocurrencias de una palabra
palabra_a_buscar = 'y'
conteo = 0
for palabra in lista_de_palabras:
    if palabra_a_buscar == palabra:
        conteo += 1
print('la palabra <<{}>> esta {} vez/veces'.format(palabra_a_buscar, conteo))
print('FIN - BLOQUE 3' + '\n')

# Bloque 4 - Palabras que empiezan con una letra
primera_letra = 'c'
lista_de_palabras_econtradas = []
for palabra in lista_de_palabras:
    if primera_letra == palabra[0]:
        lista_de_palabras_econtradas.append(palabra)

print('Palabras que empiezan con "{}":'.format(primera_letra))
print(lista_de_palabras_econtradas)
print('FIN - BLOQUE 4' + '\n')
