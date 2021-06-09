import math


class Salida:

    direccion = ""
    posicion = None


class Indicador:
    def __init__(self, inicio):
        self._ON = inicio
        self._estado = 'Sin Estado'

    def setear(self, valor):
        if self._ON == 'ON':
            self._estado = valor


class Comparador:

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, posicion):

        resultado = "Quieto"
        if posicion != self._referencia:
            resultado = "Subir" if posicion < self._referencia else "Bajar"
        return resultado


class Actuador:

    def __init__(self, tope1, tope2):
        self._tope1 = tope1
        self._tope2 = tope2
        self._indicador = Indicador('ON')

    def accionar(self, direccion):
        print(direccion)

    def alertar(self, posicion):
        if self.esta_cerca_del_tope(posicion, self._tope1) or self.esta_cerca_del_tope(posicion, self._tope2):
            self._indicador.setear("Apagado")
        else:
            self._indicador.setear("Prendido")

    def esta_cerca_del_tope(self, posicion, tope):
        return math.fabs(posicion - tope) < 3

class Control:

    def __init__(self):
        self.mi_comparador = Comparador(10)
        self.mi_actuador = Actuador(15, 5)

    def mover(self, salida):
        salida.Indicador = self.mi_actuador.alertar(salida.posicion)
        print(salida.Indicador)
        self.mi_actuador.accionar(self.mi_comparador.comparar(salida.posicion))


if __name__ == "__main__":
    mi_salida = Salida()
    mi_salida.posicion = 7
    mi_control = Control()
    mi_control.mover(mi_salida)