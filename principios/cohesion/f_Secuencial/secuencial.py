'''

class adquisicion(object):

    def adquirir(self):
        return senial


class filtrado(object):

    def filtrar(self, senial):
        return senial

class proceso(object):

    def procesar(self, senial):
        return senial

class guardado(object):

    def guardar(self, senial):
        return senial


class controlador(object):

    def __init__(self):
        self._a = adquisicion()
        self._f = filtrado()
        self._p = proceso()
        self._g = guardado()

    def ejecutar(self):

        senial_a = self._a.adquirir()
        senial_f = self._f.filtrar(senial_a)
        senial_p = self._p.procesar(senial_f)
        senial_g = self._g.guardar(senial_p)
        print(senial_g, "guardada")
'''


