class TipoD:

    def __init__(self):
        self._accion = 'creando'
        print('Tipo D. Accion: {0}'.format(self._accion))

    def hacer(self):
        self._accion = 'haciendo'
        print('Tipo D. Accion: {0}'.format(self._accion))


class TipoC:

    def __init__(self):
        self._accion = 'creando'
        self._tipo = None
        print('Tipo C. Accion: {0}'.format(self._accion))

    def resolver(self):
        self._accion = 'haciendo algo'
        print('Tipo C. Accion: {0}'.format(self._accion))

    def delegar(self):
        self._tipo.hacer()

    def asignar(self, tipo):
        self._tipo = tipo


if __name__ == '__main__':
    c = TipoC()
    c.resolver()
    c.asignar(TipoD())
    c.delegar()
