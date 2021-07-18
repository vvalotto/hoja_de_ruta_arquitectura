"""

"""
from PatronesGRASP.grasp.presupuesto.entidades.cuenta_gasto_asigando import *
from PatronesGRASP.grasp.presupuesto.aplicacion.notificador import *


class ValidadorGastoPresupuesto:

    def __init__(self, presupuesto, gasto_asignado, notificador):
        self.__presupuesto = presupuesto
        self.__gasto_asignado = gasto_asignado
        self.__nofificador = notificador

    def validar(self):
        for cuenta_gasto_asignado in self.__gasto_asignado.obtener_cuentas():
            print(cuenta_gasto_asignado.gasto_asignado)

            cuenta_presupuestada = self.__presupuesto.obtener_cuenta(cuenta_gasto_asignado.id)
            if cuenta_presupuestada is not None:
                if cuenta_presupuestada.obtener_presupuesto_cuenta() > cuenta_gasto_asignado.gasto_asignado:
                    self._notificar("Cuenta: " + cuenta_presupuestada.id + ", Fuera de presupuesto asigando")

    def _notificar(self, mensaje):
        self.__nofificador.notificar(mensaje)