
class Comparador:

    def __init__(self, referencia):
        self._referencia = referencia

    def comparar(self, valor):

        resultado = "Quieto"
        if valor != self._referencia:
            resultado = "Subir" if valor < self._referencia else "Bajar"
        return resultado


class Actuador:

    def accionar(self, accion):
        print(accion)


class Control:

    def __init__(self):
        self._comparador = Comparador(10)
        self._actuador = Actuador()

    def mover(self, posicion_deseada):
        self._actuador.accionar(self._comparador.comparar(posicion_deseada))


if __name__ == "__main__":
    mi_control = Control()
    mi_control.mover(10)

