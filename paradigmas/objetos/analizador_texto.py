"""
Clase que trata el análisis del un texto de acuerdo al problema presentado
"""


class AnalizadorTexto:

    @property
    def texto(self):
        return self._texto

    def __init__(self, texto):

        self._texto = texto
        self._lista_de_palabras = []

    def _filtrar_caracteres_alfabeticos(self):
        """
        Elimina los caracteres que no son alfabeticos en el texto
        :return: Texto sin caracteres especiales o de puntuación
        """
        caracteres_descartables = [',', '.', ':', ';', '-', '_']
        texto_filtrado = ''
        for caracter in self._texto:
            if caracter not in caracteres_descartables:
                texto_filtrado += caracter

        return texto_filtrado

    def _depurar_texto(self):
        """
        Pasa las palabras del texto a minuscula
        :return: texto sin minúscula
        """
        texto_con_palabras = self._filtrar_caracteres_alfabeticos()
        texto_con_palabras_en_minusculas = texto_con_palabras.lower()

        return texto_con_palabras_en_minusculas

    def obtener_palabras(self):
        """
        Genera un lista de palabras desde un texto
        :return: lista de palabras
        """
        texto_depurado = self._depurar_texto()
        self._lista_de_palabras = texto_depurado.split()

        return self._lista_de_palabras

    def contar_palabras(self):
        """
        Cuenta las palabras de un texto
        :return: Cantidad de palabras
        """
        return len(self._lista_de_palabras)

    def obtener_palabras_iniciadas_con(self, letra):
        """
        Obtiene una lista de palabras que empiezan con una letra definida
        :param letra: letra que se quiere buscar en cada palabra del texto
        :return: lista de palabras
        """
        lista_de_palabras = []
        for palabra in self._lista_de_palabras:
            if palabra[0] == letra:
                lista_de_palabras.append(palabra)

        return lista_de_palabras

    def contar_palabras_iniciadas_con(self, letra):
        """
        Cuenta la cantidad de palabras de un texto que empiezan con la letra definida
        :param letra: letra que se quiere buscar en cada palabra del texto
        :return: cantidad de palabras encontradas
        """
        return len(self.obtener_palabras_iniciadas_con(letra))
