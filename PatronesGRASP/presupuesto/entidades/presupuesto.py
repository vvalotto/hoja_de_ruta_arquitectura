"""
Clase Presupuesto de gastos
Mantiene el presupuesto de cuentas contables de una gerencia definida
"""


class Presupuesto:

    def __init__(self, gerencia):
        self.__sector = gerencia
        self.__anio = 2021
        self.__cuentas = []

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def obtener_cuenta(self, identificacion):
        for cuenta in self.__cuentas:
            if cuenta.id == identificacion:
                return cuenta
            else:
                return None

    def eliminar_cuenta(self, identificacion):
        for cuenta in self.__cuentas:
            if identificacion == cuenta.identificacion:
                self.__cuentas.remove(cuenta)
                return
        return None

    def obtener_presupuesto(self):
        valor_presupuesto = 0
        for cuenta in self.__cuentas:
            valor_presupuesto += cuenta.obtener_presupuesto_cuenta()
        return valor_presupuesto
