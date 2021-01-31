import math


class Salida:

    direccion = ""
    Indicador = ""
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

    def actuar(self, salida):
        print(salida.direccion)

    def alertar(self, salida):
        if math.fabs(salida.posicion - self._tope1) > 2:
            salida.Indicador = "Apagado"
        else:
            salida.Indicador = "Prendido"
        print(salida.Indicador)


class Control:

    def __init__(self):
        self.mi_comparador = Comparador(10)
        self.mi_actuador = Actuador(15, 5)

    def mover(self, salida):
        self.mi_actuador.alertar(salida)
        self.mi_actuador.actuar(self.mi_comparador.comparar(salida))


if __name__ == "__main__":
    mi_salida = Salida()
    mi_salida.posicion = 14
    mi_control = Control()
    mi_control.mover(mi_salida)
