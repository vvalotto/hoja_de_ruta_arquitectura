"""

"""

from .linea_prespuesto import *


class CuentaPresupuesto:

    def __init__(self, id):
        self._identificacion = id
        self._lineas_presupuesto = []

    def crear_linea(self, descripcion_linea):
        self._lineas_presupuesto.append(LineaPresupuesto(descripcion_linea))

    def obtener_linea(self, descripcion_linea):
        return

    def actualizar_linea(self, descripcion_linea):
        return

    def eliminar_linea(self, descripcion_linea):
        pass

    def obtener_presupuesto_cuenta(self):
        return