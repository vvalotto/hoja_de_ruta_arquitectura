from PatronesGRASP.grasp.presupuesto.entidades.presupuesto import *
from PatronesGRASP.grasp.presupuesto.aplicacion.cuenta_controlador import *
from PatronesGRASP.grasp.presupuesto.aplicacion.validador import *

# Crear el presupuesto
mi_presupuesto = Presupuesto("TI")


cuenta_control = CuentaPresupuestoControlador()
cuenta_control.crear_cuenta('1000', 'Servicios Tecnolgicos')
cuenta_control.agregar_linea('Mant1')
cuenta_control.agregar_linea('Lic1')

# Agregar Cuenta al presupuesto
mi_presupuesto.agregar_cuenta(cuenta_control.cuenta)

mi_cuenta = mi_presupuesto.obtener_cuenta('1000')
print(mi_cuenta)

for linea in mi_cuenta.obtener_lineas_presupuesto():
    print(linea.denominacion)
    print(linea.obtener_presupuesto_linea())

    if linea.denominacion == 'Mant1':
        gasto = Gasto(1200)
        for mes in Meses().meses:
            linea.presupuestar_mes(mes, gasto)
    elif linea.denominacion == 'Lic1':
        gasto1 = GastoOtraMoneda(100, 'U$S')
        gasto1.tipo_de_cambio = 80
        linea.presupuestar_mes('Enero', gasto1)
        gasto2 = GastoOtraMoneda(100, 'U$S')
        gasto2.tipo_de_cambio = 82
        linea.presupuestar_mes('Febrero', gasto2)
        gasto3 = GastoOtraMoneda(100, 'U$S')
        gasto3.tipo_de_cambio = 84
        linea.presupuestar_mes('Marzo', gasto3)
        gasto4 = GastoOtraMoneda(100, 'U$S')
        gasto4.tipo_de_cambio = 86
        linea.presupuestar_mes('Abril', gasto4)
        gasto5 = GastoOtraMoneda(100, 'U$S')
        gasto5.tipo_de_cambio = 88
        linea.presupuestar_mes('Mayo', gasto5)
        gasto6 = GastoOtraMoneda(100, 'U$S')
        gasto6.tipo_de_cambio = 90
        linea.presupuestar_mes('Junio', gasto6)

for linea in mi_cuenta.obtener_lineas_presupuesto():
    print(linea.denominacion + ': ' + str(linea.obtener_presupuesto_linea()))

print(mi_cuenta.descripcion + ": " + str(mi_cuenta.obtener_presupuesto_cuenta()))
print(cuenta_control.obtener_prespuesto())

# Validador
notificador = Notificador()
gasto_asignado_2021 = GastoAsignado()
cuenta_1000 = CuentaGastoAsignado('1000', 50000)
cuenta_1001 = CuentaGastoAsignado('1001', 300000)

gasto_asignado_2021.agregar_cuenta(cuenta_1001)
gasto_asignado_2021.agregar_cuenta(cuenta_1000)


validador_presupuesto = ValidadorGastoPresupuesto(mi_presupuesto, gasto_asignado_2021, notificador)
validador_presupuesto.validar()