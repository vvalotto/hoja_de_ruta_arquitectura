
class TipoM:

    def __init__(self):
        self._accion = 'creando M'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))

    def hacer(self):
        self._accion = 'haciendo M'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))


class TipoN(TipoM):

    def resolver(self):
        self._accion = 'haciendo algo N'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))


if __name__ == '__main__':
    m = TipoM()
    m.hacer()
    n = TipoN()
    n.hacer()
    n.resolver()
