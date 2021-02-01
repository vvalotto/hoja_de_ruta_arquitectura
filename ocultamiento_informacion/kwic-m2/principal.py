"""

"""


from ingreso.ingreso import *
from rotador.rotador import *
from ordenador.ordenador import *
from visualizador.visualizador import *

lineas = leer_linea_texto('texto.txt')
mi_rotador = Rotador(lineas)
mi_rotador.armar_cadenas_circulares()
mi_rotador.generar_indices_de_palabras()
mi_alfabetizador = Alfabetizador(mi_rotador)
mi_alfabetizador.armar_lista_palabras_clave()
visualizar(mi_alfabetizador.armar_frases_contexto())
