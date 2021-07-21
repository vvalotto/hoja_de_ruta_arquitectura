"""
Clase encargada de guardar las Cuentas Presupuestadas
"""
import pickle


class CuentaPresupuestoPersistidor:

    def __init__(self, ubicacion):
        self._ubicacion = ubicacion

    def guardar(self, cuenta):
        id_cuenta = cuenta.id
        try:
            cuenta_archivo = open(self._ubicacion + "/" + str(id_cuenta), 'ab')
            pickle.dump(cuenta, cuenta_archivo)
            cuenta_archivo.close()
        except IOError:
            print('Error al grabar la linea')

    def recuperar(self, id_cuenta):
        cuenta = None
        try:
            cuenta_archivo = open(self._ubicacion + "/" + str(id_cuenta), 'rb')
            cuenta = pickle.load(cuenta_archivo)
            cuenta_archivo.close()
        except IOError:
            print('Error al leer la linea')
        return cuenta
