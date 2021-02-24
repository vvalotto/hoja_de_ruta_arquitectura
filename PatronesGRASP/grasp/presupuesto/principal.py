from controladores.cuenta_controlador import *

cuenta_control = CuentaPresupuestoControlador()
cuenta_control.crear_cuenta('1000')
cuenta_control.agregar_linea('Mant1')
linea_presupuesto = cuenta_control.obtener_linea('Mant1')
for mes in linea_presupuesto.obtener_gasto_meses():
    print(mes)
linea_presupuesto.presupuestar_mes('Enero', 100)
linea_presupuesto.presupuestar_mes('Febrero', 200)
for mes in linea_presupuesto.obtener_gasto_meses():
    print(mes)
print(cuenta_control.obtener_prespuesto())