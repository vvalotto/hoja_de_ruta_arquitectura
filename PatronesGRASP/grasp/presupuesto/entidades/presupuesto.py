"""

"""

from .cuenta_presupuesto import *


class Presupuesto:

    def __init__(self, sector):
        self._sector = sector
        self._cuentas = []

    def crear_cuenta(self, descripcion_cuenta):
        self._cuentas.append(LineaPresupuesto(descripcion_cuenta))

    def obtener_cuenta(self, descripcion_cuenta):
        return

    def eliminar_cuenta(self, descripcion_cuenta):
        pass

    def obtener_presupuesto_sector(self):
        pass
