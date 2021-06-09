class TipoG:

    def __init__(self):
        self._accion = 'creando'
        print('Tipo G. Accion: {0}'.format(self._accion))

    def hacer(self):
        self._accion = 'haciendo'
        print('Tipo G. Accion: {0}'.format(self._accion))


class TipoH:

    def __init__(self, tipo):
        self._accion = 'creando'
        self._tipo = tipo
        print('Tipo H. Accion: {0}'.format(self._accion))

    def resolver(self):
        self._tipo.hacer()
        self._accion = 'haciendo algo'
        print('Tipo H. Accion: {0}'.format(self._accion))


if __name__ == '__main__':
    h = TipoH(TipoG())
    h.resolver()
