"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio
"""


class Senial:
    """
    Definicion de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valor(indice)
    -> obtener_tamanio()
    """
    
    def __init__(self):
        """
        Constructor: Inicializa la lista de valores vacia
        """
        self._valores = []
    
    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self._valores.append(valor)
    
    def obtener_valor(self, indice):
        """
        Recupera el contenido según el indice
        :param indice:
        :return: Valor
        """
        try:
            valor = self._valores[indice]
            return valor
        except Exception as ex:
            print('Error: ', ex.args)
            return None

    def obtener_tamanio(self):
        """
        Retorna el largo de la lista de valores
        :return:
        """
        return len(self._valores)
