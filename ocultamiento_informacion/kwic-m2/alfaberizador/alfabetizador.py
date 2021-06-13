"""
Módulo que genera todas las frase en contexto ordenado alfabeticamente por palabra clave que inicia cada frase
"""


class Alfabetizador:
    """
    Ordena alfabeticamente la lista de palabras clave, con su renglon y
    posicion en la frase
    """
    def __init__(self, rotador, indexador):
        self._rotador = rotador
        self._indexador = indexador
        self._palabras_clave_ordenadas = []

    def armar_lista_palabras_clave(self):
        lista_indices = self._indexador.obtener_indices_de_palabras()
        for numero_linea in range(0, len(lista_indices)):
            linea = self._rotador.obtener_linea(numero_linea)
            indices = lista_indices[numero_linea]
            for indice in indices:
                self._palabras_clave_ordenadas.append([linea.obtener_palabra(indice),
                                                       numero_linea,
                                                       indice
                                                       ])
        self._ordenar_palabras_clave()

    def _ordenar_palabras_clave(self):
        lista = self._palabras_clave_ordenadas

        for puntero_a in range(0, len(lista)):
            for puntero_b in range(puntero_a + 1, len(lista)):
                if lista[puntero_a][0] > lista[puntero_b][0]:
                    elemento_seleccionado = lista[puntero_b]
                    lista[puntero_b] = lista[puntero_a]
                    lista[puntero_a] = elemento_seleccionado

    def obtener_lista_palabras_clave(self):
        return self._palabras_clave_ordenadas

    def armar_frases_contexto(self):
        """
        Para cada palabra clave obtener la frase en contexto
        """
        frases_en_contexto = []
        for palabra_clave in self._palabras_clave_ordenadas:
            renglon = palabra_clave[1]
            posicion = palabra_clave[2]
            frases_en_contexto.append(self._rotador.obtener_linea_rotada(renglon, posicion))
        return frases_en_contexto
