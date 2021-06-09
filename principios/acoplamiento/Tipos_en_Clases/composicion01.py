class TipoF:

    def __init__(self):
        self._accion = 'creando'
        print('Tipo F. Accion: {0}'.format(self._accion))

    def hacer(self):
        self._accion = 'haciendo'
        print('Tipo F. Accion: {0}'.format(self._accion))


class TipoE:

    def __init__(self):
        self._accion = 'creando'
        self._tipo = TipoF()
        print('Tipo E. Accion: {0}'.format(self._accion))

    def resolver(self):
        self._tipo.hacer()
        self._accion = 'haciendo algo'
        print('Tipo E. Accion: {0}'.format(self._accion))


if __name__ == '__main__':
    e = TipoE()
    e.resolver()
