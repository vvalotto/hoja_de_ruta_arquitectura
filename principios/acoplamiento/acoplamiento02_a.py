import math


class Salida:

    direccion = ""
    indicador = ""
    posicion = None


class Comparador:

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, salida):

        resultado = "Quieto"
        if salida.posicion != self._referencia:
            resultado = "Subir" if salida.posicion < self._referencia else "Bajar"
        salida.direccion = resultado
        return salida


class Actuador:

    def __init__(self, tope1, tope2):
        self._tope1 = tope1
        self._tope2 = tope2

    def accionar(self, salida):
        print(salida.direccion)

    def alertar(self, salida):

        if self.esta_cerca_del_tope(salida, self._tope1) or self.esta_cerca_del_tope(salida, self._tope2):
            salida.indicador = "Prendido"
        else:
            salida.indicador = "Apagado"
        print(salida.indicador)

    def esta_cerca_del_tope(self, salida, tope):
        return math.fabs(salida.posicion - tope) < 3


class Control:

    def __init__(self):
        self._comparador = Comparador(10)
        self._actuador = Actuador(15, 5)

    def mover(self, salida):
        self._actuador.alertar(salida)
        self._actuador.accionar(self._comparador.comparar(salida))


if __name__ == "__main__":
    mi_salida = Salida()
    mi_salida.posicion = 6
    mi_control = Control()
    mi_control.mover(mi_salida)
