import math


class Salida(object):

    direccion = ""
    posicion = None


class Indicador(object):
    def __init__(self):
        self._estado = 'Sin Estado'

    def on(self):
        self._estado = 'ON'
        print(self._estado)

    def off(self):
        self._estado  = 'OFF'
        print(self._estado)

    def titilar(self):
        self._estado = 'titilar'
        print(self._estado)


class Comparador(object):

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, posicion):

        resultado = "Quieto"
        if posicion != self._referencia:
            resultado = "Subir" if posicion < self._referencia else "Bajar"
        return resultado


class Actuador(object):

    def __init__(self, tope1, tope2):
        self._tope1 = tope1
        self._tope2 = tope2
        self.mi_indicador = Indicador()
        self.mi_indicador.off()

    def actuar(self, direccion):
        print(direccion)

    def alertar(self, posicion):
        if math.fabs(posicion - self._tope1) > 2:
            self.mi_indicador.titilar()
        else:
            self.mi_indicador.on()
        return self.mi_indicador


class Control(object):

    def __init__(self):
        self.mi_comparador = Comparador(10)
        self.mi_actuador = Actuador(15, 5)

    def mover(self, salida):
        salida.Indicador = self.mi_actuador.alertar(salida.posicion)
        print(salida.Indicador)
        self.mi_actuador.actuar(self.mi_comparador.comparar(salida.posicion))


if __name__ == "__main__":
    mi_salida = Salida()
    mi_salida.posicion = 15
    mi_control = Control()
    mi_control.mover(mi_salida)
