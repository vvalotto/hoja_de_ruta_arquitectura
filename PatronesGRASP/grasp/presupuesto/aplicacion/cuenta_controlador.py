"""

"""
from PatronesGRASP.grasp.presupuesto.entidades.cuenta_presupuesto import *


class CuentaPresupuestoControlador:

    @property
    def cuenta(self):
        return self._cuenta

    def __init__(self):
        self._cuenta = None

    def crear_cuenta(self, identificacion_cuenta, descripcion):
        self._cuenta = CuentaPresupuesto(identificacion_cuenta, descripcion)

    def agregar_linea(self, denominacion_linea):
        self._cuenta.crear_linea(denominacion_linea)

    def actualizar_linea(self, denominacion_linea):
        self._cuenta.actualizar_linea(denominacion_linea)

    def obtener_linea(self, denominacion_linea):
        return self._cuenta.obtener_linea(denominacion_linea)

    def obtener_prespuesto(self):
        return self._cuenta.obtener_presupuesto_cuenta()
