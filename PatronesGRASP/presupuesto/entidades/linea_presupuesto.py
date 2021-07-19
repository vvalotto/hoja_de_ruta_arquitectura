"""
Linea de gasto anual a prespuestar.
Corresponde a un servicio, licencia, contrado.
Se especifica por su denominacion que respresenta el gasto
"""

from .gasto_mensual import *


class LineaPresupuesto:

    @property
    def denominacion(self):
        return self.__denominacion

    def __init__(self, denominacion):
        self.__denominacion = denominacion
        self.__gasto_anual = []

        for mes in Meses().meses:
            self.__gasto_anual.append(GastoMensual(mes))

    def presupuestar_mes(self, mes, valor_gasto):
        for gasto_mensual in self.__gasto_anual:
            if mes == gasto_mensual.mes:
                gasto_mensual.gasto = valor_gasto
                break

    def obtener_presupuesto_mes(self, mes):
        for gasto_mensual in self.__gasto_anual:
            if mes == gasto_mensual.mes:
                return gasto_mensual.gasto

    def obtener_presupuesto_linea(self):
        gasto_linea = 0
        for gasto_mensual in self.__gasto_anual:
            gasto_linea += gasto_mensual.gasto.cantidad
        return gasto_linea

    def obtener_gasto_meses(self):
        return self.__gasto_anual
