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

    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self._valores.append(valor)
        self._cantidad += 1
        return
    
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


class SenialPila(Senial):
    """
    Clase de tipo Pila que hereda de la clase senial los miembros variables de instancia
    y extiende el metodo para sacar datos
    """
    def sacar_valor(self):
        try:
            if self._cantidad != 0:
                self._cantidad -= 1
                return self._valores[self._cantidad]
            else:
                raise Exception('No hay valores para sacar')
        except Exception as e:
            print('Error ;', e)


class SenialCola(Senial):
    """
    Clase de tipo Cola que hereda de la clase senial los miembros variables de instancia
    y extiende el metodo para sacar datos
    """
    def __init__(self, tamanio):
        """
        Construye la instancia de la estructura cola circular, donde se indica el
        tamanio de la cola y se inicializan los punteros de la cabeza y cola
        :param tamanio:
        :return:
        """
        super().__init__(tamanio)
        self._cabeza = 0
        self._cola = 0
        # Se crea la cola vacia pero con lugares para poner valores
        for i in range(0, tamanio):
            self._valores.append(None)

    def sacar_valor(self):
        try:
            if (self._cabeza != self._cola) or ((self._cabeza == self._cola) and (self._cantidad != 0)):
                valor = self._valores[self._cabeza]
                if self._cabeza == (self._tamanio - 1):
                    self._cabeza = 0
                else:
                    self._cabeza += 1
                self._cantidad -= 1
                return valor
            else:
                raise Exception('No hay valores para sacar')
        except Exception as e:
            print('Error ;', e)
