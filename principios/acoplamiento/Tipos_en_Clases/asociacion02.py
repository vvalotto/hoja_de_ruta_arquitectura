class TipoA:

    def __init__(self):
        self._accion = 'creando'
        print('Tipo A. Accion: {0}'.format(self._accion))

    def hacer(self):
        self._accion = 'haciendo'
        print('Tipo A. Accion: {0}'.format(self._accion))


class TipoB:

    def __init__(self):
        self._accion = 'creando'
        print('Tipo B. Accion: {0}'.format(self._accion))

    def resolver(self):
        t = TipoA()
        t.hacer()
        self._accion = 'haciendo algo'
        print('Tipo B. Accion: {0}'.format(self._accion))


if __name__ == '__main__':
    b = TipoB()
    b.resolver()
