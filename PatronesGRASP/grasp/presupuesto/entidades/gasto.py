"""

"""


class Gasto:

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def moneda(self):
        return self._moneda

    def __init__(self, cantidad):
        self._cantidad = cantidad
        self._moneda = "$"

    def __str__(self):
        return self._moneda + " " + str(self._cantidad)


class GastoOtraMoneda(Gasto):

    @property
    def cantidad(self):
        return self._cantidad * self._tipo_de_cambio

    @property
    def gasto_moneda_origen(self):
        return self._cantidad

    @property
    def tipo_de_cambio(self):
        return self._tipo_de_cambio

    @tipo_de_cambio.setter
    def tipo_de_cambio(self, valor):
        self._tipo_de_cambio = valor

    def __init__(self, cantidad, moneda):
        super(GastoOtraMoneda, self).__init__(cantidad)
        self._moneda = moneda
        self._tipo_de_cambio = 1

