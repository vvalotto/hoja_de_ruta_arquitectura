"""
Clase que corresponde a una cuenta contable del presupuesto.
Esta cuenta posee una o mas lineas a presupuestar.
No es posible definir una cuenta sin linea presupuestaria.
"""

from .linea_prespuesto import *


class CuentaPresupuesto:

    @property
    def id(self):
        return self._identificacion

    def __init__(self, identificacion):
        self._identificacion = identificacion
        self._lineas_presupuesto = []

    def crear_linea(self, descripcion_linea):
        self._lineas_presupuesto.append(LineaPresupuesto(descripcion_linea))

    def obtener_linea(self, descripcion_linea):
        for linea in self._lineas_presupuesto:
            if descripcion_linea == linea.denominacion:
                return linea
        return None

    def actualizar_linea(self, linea_actualizada):
        for linea in self._lineas_presupuesto:
            if linea_actualizada.denominacion == linea.denominacion:
                indice = self._lineas_presupuesto.index(linea)
                self._lineas_presupuesto[indice] = linea_actualizada
                return
        return

    def eliminar_linea(self, descripcion_linea):
        for linea in self._lineas_presupuesto:
            if descripcion_linea == linea.denominacion:
                self._lineas_presupuesto.remove(linea)
                return
        return

    def obtener_presupuesto_cuenta(self):
        presupuesto = 0
        for linea in self._lineas_presupuesto:
            presupuesto += linea.obtener_presupuesto_linea()
        return presupuesto

    def obtener_lineas_presupuesto(self):
        return self._lineas_presupuesto