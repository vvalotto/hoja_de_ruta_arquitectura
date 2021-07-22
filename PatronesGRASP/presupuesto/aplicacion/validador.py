"""
Validar de gastos presupuestados
"""


class ValidadorGastoPresupuesto:

    def __init__(self, presupuesto, gasto_asignado):
        self.__presupuesto = presupuesto
        self.__gasto_asignado = gasto_asignado

    def validar(self):
        for cuenta_gasto_asignado in self.__gasto_asignado.obtener_cuentas():
            print(cuenta_gasto_asignado.gasto_asignado)

            cuenta_presupuestada = self.__presupuesto.obtener_cuenta(cuenta_gasto_asignado.id)
            if cuenta_presupuestada is not None:
                if cuenta_presupuestada.obtener_presupuesto_cuenta() > cuenta_gasto_asignado.gasto_asignado:
                    self.__notificar("Cuenta: " + cuenta_presupuestada.id + ", Fuera de presupuesto asigando")

    def __notificar(self, mensaje):
        print(mensaje)