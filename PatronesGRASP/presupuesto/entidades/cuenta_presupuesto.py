"""
Clase que corresponde a una cuenta contable del presupuesto.
Esta cuenta posee una o mas lineas a presupuestar.
"""

from PatronesGRASP.presupuesto.entidades.linea_presupuesto import *


class CuentaPresupuesto:

    @property
    def id(self):
        return self.__identificacion

    @property
    def descripcion(self):
        return self.__descrpcion

    def __init__(self, identificacion, descripcion):
        self.__identificacion = identificacion
        self.__descrpcion = descripcion
        self.__lineas_presupuesto = []

    def crear_linea(self, descripcion_linea):
        self.__lineas_presupuesto.append(LineaPresupuesto(descripcion_linea))

    def obtener_linea(self, descripcion_linea):
        for linea in self.__lineas_presupuesto:
            if descripcion_linea == linea.denominacion:
                return linea
        return None

    def actualizar_linea(self, linea_actualizada):
        for linea in self.__lineas_presupuesto:
            if linea_actualizada.denominacion == linea.denominacion:
                indice = self.__lineas_presupuesto.index(linea)
                self.__lineas_presupuesto[indice] = linea_actualizada
                return
        return

    def eliminar_linea(self, descripcion_linea):
        for linea in self.__lineas_presupuesto:
            if descripcion_linea == linea.denominacion:
                self.__lineas_presupuesto.remove(linea)
                return
        return

    def obtener_presupuesto_cuenta(self):
        presupuesto = 0
        for linea in self.__lineas_presupuesto:
            presupuesto += linea.obtener_presupuesto_linea()
        return presupuesto

    def obtener_lineas_presupuesto(self):
        return self.__lineas_presupuesto

    def __str__(self):
        return self.__identificacion + ':' + self.__descrpcion
