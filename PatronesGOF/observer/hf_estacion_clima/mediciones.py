

class Temperatura:

    @property
    def medicion(self):
        return self._medicion

    def __init__(self):
        self._medicion = None

    def leer(self):
        with open('temperatura.dat', 'r') as medicion:
            self._medicion = medicion.readline()


class Humedad:

    @property
    def medicion(self):
        return self._medicion

    def __init__(self):
        self._medicion = None

    def leer(self):
        with open('humedad.dat') as medicion:
            self._medicion = medicion.read()

class Presion:

    @property
    def medicion(self):
        return self._medicion

    def __init__(self):
        self._medicion = None

    def leer(self):
        with open('presion.dat') as medicion:
            self._medicion = medicion.read()