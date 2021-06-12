"""
Programa principal
"""


from ingreso.ingreso import leer_linea_texto
from rotador.rotador import Rotador
from indexador.indexador import Indexador
from alfaberizador.alfabetizador import Alfabetizador
from visualizador.visualizador import visualizar

lineas = leer_linea_texto('texto.txt')

mi_rotador = Rotador(lineas)
mi_rotador.armar_cadenas_circulares()

mi_indexador = Indexador(lineas)
mi_indexador.generar_indices_de_palabras()

mi_alfabetizador = Alfabetizador(mi_rotador, mi_indexador)
mi_alfabetizador.armar_lista_palabras_clave()

visualizar(mi_alfabetizador.armar_frases_contexto())
