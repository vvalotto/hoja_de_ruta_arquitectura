"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio

Modificacion: Se crea un clase abstracta que define todas las interfaces de las
estructuras de las seniales y resuelve la violacion de los principio OCP y LSP
"""

from abc import abstractmethod


class SenialBase(object):
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
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self._fecha_adquisicion = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, datos):
        self._valores = datos

    def __init__(self, tamanio=10):
        """
        Constructor: Inicializa la lista de valores vacia
        :return:
        """
        self._valores = []
        self._fecha_adquisicion = None
        self._cantidad = 0
        self._tamanio = tamanio
        return

    @abstractmethod
    def poner_valor(self, valor):
        pass

    @abstractmethod
    def sacar_valor(self):
        pass

    def limpiar(self):
        """
        Deja a la senial sin valores
        """
        self._valores.clear()
        self._cantidad = 0
    
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

    def __str__(self):
        cad = ""
        cad += "tamanio: " + str(self._tamanio) + "\n"
        cad += "fecha_adquisicion: " + str(self._fecha_adquisicion)
        return cad


class SenialLista(SenialBase):
    """
    Clase tipo lista que implementa los metodos de manipulacion de datos
    dentro de la estructura
    """
    def __init__(self, tamanio=10):
        super().__init__(tamanio)
        self._indice = 0
        return

    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        """
        Por se una lista se trata como un arreglo. No se saca literalmente el dato sino
        que se obtiene desde el indice inicial hasta el último
        :return:
        """
        valor = 0
        if self._indice < self.cantidad:
            indice = self._indice
            valor = self.obtener_valor(indice)
            self._indice += 1
        else:
            print('Error: No hay nada para sacar')
        return valor


class SenialPila(SenialBase):
    """
    Clase no implementada
    """
    pass


class SenialCola(SenialBase):
    """
    Clase no implementada
    """
    pass
