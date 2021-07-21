from PatronesGRASP.presupuesto.aplicacion.cuenta_controlador import *


"""
Se crean los gastos objetivos o asignados para cada cuenta
"""
from PatronesGRASP.presupuesto.entidades.presupuesto import *

# Crear el presupuesto
mi_presupuesto = Presupuesto("TI")

# Crear el controlador de Cuenta Contable
cuenta_controlador = CuentaPresupuestoControlador()
# Crear la cuenta a traves del controlador
cuenta_controlador.crear_cuenta('1000', 'Servicios Tecnolgicos')
# LLenar las cuenta con las lineas de gastos a través del controlador
cuenta_controlador.agregar_linea('Mant1')
cuenta_controlador.agregar_linea('Lic1')

# Agregar Cuenta al presupuesto
mi_presupuesto.agregar_cuenta(cuenta_controlador.cuenta)

# Llenar la cuenta conta
mi_cuenta = mi_presupuesto.obtener_cuenta('1000')
print(mi_cuenta)

#
for linea in mi_cuenta.obtener_lineas_presupuesto():
    print(linea.denominacion)
    print(linea.obtener_presupuesto_linea())

    # Linea con gastos en Pesoso
    if linea.denominacion == 'Mant1':
        gasto = Gasto(1200)
        for mes in Meses().meses:
            linea.presupuestar_mes(mes, gasto)
    # Linea con gastos en Dolares
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
print(cuenta_controlador.obtener_prespuesto())

# Almacenar la cuenta presupuestada
cuenta_controlador.persistir_cuenta()

# Recuperar la cuenta en otro controlador
otra_cuenta_controlador = CuentaPresupuestoControlador()
otra_cuenta_controlador.recuperar_cuenta('1000')
print("Otro controdor:" + str(otra_cuenta_controlador.obtener_prespuesto()))
