from aplicacion.cuenta_controlador import *
from aplicacion.validador import *
from persistencia.gasto_mensual_persistidor import *

"""
Se crean los gastos objetivos o asignados para cada cuenta
"""

gasto_asignado_2021 = GastoAsignado()
cuenta_1000 = CuentaGastoAsignado('1000', 200000)
cuenta_1001 = CuentaGastoAsignado('1001', 300000)

gasto_asignado_2021.agregar_cuenta(cuenta_1001)
gasto_asignado_2021.agregar_cuenta(cuenta_1000)
# ----------------------------------------------------

cuenta_control = CuentaPresupuestoControlador()
cuenta_control.crear_cuenta('1000', 'Servicios Tecnoligicos')
cuenta_control.agregar_linea('Mant1')
cuenta_control.agregar_linea('Lic1')

linea_presupuesto = cuenta_control.obtener_linea('Mant1')

for mes in linea_presupuesto.obtener_gasto_meses():
    print(mes)
linea_presupuesto.presupuestar_mes('Enero', 100)
linea_presupuesto.presupuestar_mes('Febrero', 200)

for mes in linea_presupuesto.obtener_gasto_meses():
    print(mes)
print(cuenta_control.obtener_prespuesto())

persistidor = CuentaPresupuestoPersistidor('.')
persistidor.guardar(cuenta_control.cuenta)
cuenta_recuperada = persistidor.recuperar('1000')
print(cuenta_recuperada.id)

for linea in cuenta_recuperada.obtener_lineas_presupuesto():
    print(linea.denominacion)