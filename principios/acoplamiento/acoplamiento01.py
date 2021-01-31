
class Comparador:

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, valor):

        resultado = "Quieto"
        if valor != self._referencia:
            resultado = "Subir" if valor < self._referencia else "Bajar"
        return resultado


class Actuador:

    def actuar(self, accion):
        print(accion)


class Control:

    def __init__(self):
        self.mi_comparador = Comparador(10)
        self.mi_actuador = Actuador()

    def mover(self, pos_actual):
        self.mi_actuador.actuar(self.mi_comparador.comparar(pos_actual))


if __name__ == "__main__":
    mi_control = Control()
    mi_control.mover(10)

