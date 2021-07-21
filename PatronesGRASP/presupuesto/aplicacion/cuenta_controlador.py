"""
Clase que hace de intermediaria entre los eventos externos (Desde la interfaz de Usuario
o desde otro tipos clientes y las entidades de dominio.

Se agrega la gestión de la persitencia, delengado a la clase correspondiente
"""
from PatronesGRASP.presupuesto.entidades.cuenta_presupuesto import *
from PatronesGRASP.presupuesto.persistencia.cuenta_presupuesto_persistidor import *


class CuentaPresupuestoControlador:

    @property
    def cuenta(self):
        return self.__cuenta

    def __init__(self):
        self.__cuenta = None
        self.__persistidor = CuentaPresupuestoPersistidor('.')

    def crear_cuenta(self, identificacion_cuenta, descripcion):
        self.__cuenta = CuentaPresupuesto(identificacion_cuenta, descripcion)

    def agregar_linea(self, denominacion_linea):
        self.__cuenta.crear_linea(denominacion_linea)

    def actualizar_linea(self, denominacion_linea):
        self.__cuenta.actualizar_linea(denominacion_linea)

    def obtener_linea(self, denominacion_linea):
        return self.__cuenta.obtener_linea(denominacion_linea)

    def obtener_prespuesto(self):
        return self.__cuenta.obtener_presupuesto_cuenta()

    def persistir_cuenta(self):
        self.__persistidor.guardar(self.__cuenta)

    def recuperar_cuenta(self, identificador):
        self.__cuenta = self.__persistidor.recuperar(identificador)
