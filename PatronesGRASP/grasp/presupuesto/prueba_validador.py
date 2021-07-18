from PatronesGRASP.grasp.presupuesto.entidades.cuenta_gasto_asigando import *
from PatronesGRASP.grasp.presupuesto.aplicacion.validador import *
from PatronesGRASP.grasp.presupuesto.aplicacion.cuenta_controlador import *


gasto_asignado_2021 = GastoAsignado()
cuenta_1000 = CuentaGastoAsignado('1000', 200000)
cuenta_1001 = CuentaGastoAsignado('1001', 300000)

gasto_asignado_2021.agregar_cuenta(cuenta_1001)
gasto_asignado_2021.agregar_cuenta(cuenta_1000)


validador_presupuesto = ValidadorGastoPresupuesto(None, gasto_asignado_2021)
validador_presupuesto.validar()