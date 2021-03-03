from controladores.cuenta_controlador import *
from persistencia.gasto_mensual_persistidor import *

cuenta_control = CuentaPresupuestoControlador()
cuenta_control.crear_cuenta('1000')
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