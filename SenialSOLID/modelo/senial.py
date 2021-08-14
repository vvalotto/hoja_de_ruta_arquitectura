"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio

Modificacion: Se agregan miembros de instancias y se definen como propiedades
"""


class Senial(object):
    """
    Definicion de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valor(indice)
    -> obtener_tamanio()
    """

    # Propiedades
    @property
    def fecha_adquisicion(self):
        return self.__fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self.__fecha_adquisicion = valor

    @fecha_adquisicion.deleter
    def fecha_adquisicion(self):
        del self.__fecha_adquisicion

    @property
    def tamanio(self):
        return self.__cantidad

    @tamanio.setter
    def tamanio(self, valor):
        self.__cantidad = valor

    @property
    def valores(self):
        return self.__valores

    @valores.setter
    def valores(self, datos):
        self.__valores = datos

    def __init__(self):
        """
        Constructor: Inicializa la lista de valores vacia
        :return:
        """
        self.__valores = []
        self.__fecha_adquisicion = None
        self.__cantidad = 0
        return

    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self.__valores.append(valor)
        self.__cantidad += 1
        return
    
    def obtener_valor(self, indice):
        """
        Recupera el contenido según el indice
        :param indice:
        :return: Valor
        """
        try:
            valor = self.__valores[indice]
            return valor
        except Exception as ex:
            print('Error: ', ex.args)
            return None
