
class AnalizadorTexto:

    @property
    def texto(self):
        return self._texto

    def __init__(self, texto):
        self._texto = texto
        self._lista_de_palabras = []

    def _filtrar_caracteres_alfabeticos(self):

        caracteres_descartables = [',', '.', ':', ';', '-', '_']
        texto_filtrado = ''
        for caracter in self._texto:
            if caracter not in caracteres_descartables:
                texto_filtrado += caracter

        return texto_filtrado

    def _depurar_texto(self):

        texto_con_palabras = self._filtrar_caracteres_alfabeticos()
        texto_con_palabras_en_minusculas = texto_con_palabras.lower()

        return texto_con_palabras_en_minusculas

    def obtener_palabras(self):
        texto_depurado = self._depurar_texto()
        self._lista_de_palabras = texto_depurado.split()

        return self._lista_de_palabras

    def contar_palabras(self):
        return len(self._lista_de_palabras)

    def obtener_palabras_iniciadas_con(self, letra):
        lista_de_palabras = []
        for palabra in self._lista_de_palabras:
            if palabra[0] == letra:
                lista_de_palabras.append(palabra)

        return lista_de_palabras

    def contar_palabras_iniciadas_con(self, letra):
        return len(self.obtener_palabras_iniciadas_con(letra))
