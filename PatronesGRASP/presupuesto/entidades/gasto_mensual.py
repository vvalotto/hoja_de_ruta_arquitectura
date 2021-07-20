
from .meses import Meses
from .gasto import Gasto, GastoOtraMoneda


class GastoMensual:
    """
    Gasto Mensual prespuestado.
    Contiene el mes y el valor prespuestado
    """
    @property
    def mes(self):
        return self.__mes

    @property
    def gasto(self):
        return self.__gasto

    @property
    def gasto_en_pesos(self):
        return self.__gasto.cantidad

    @gasto.setter
    def gasto(self, valor):
        if valor.cantidad < 0:
            raise Exception("Error: No se pueden ingresar valores negativos")
        self.__gasto = valor

    def __init__(self, mes):
        if mes not in Meses().meses:
            raise Exception("Error: Nombre de mes inexistente")
        self.__mes = mes
        self.__gasto = Gasto(0)
        self.__ajuste = 1

    def __str__(self):
        return self.__mes + ":" + str(self.__gasto)

