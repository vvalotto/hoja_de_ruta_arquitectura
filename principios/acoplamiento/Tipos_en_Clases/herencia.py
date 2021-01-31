
class TipoY:

    def __init__(self):
        self.accion = 'creando'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return

    def hacer(self):
        self.accion = 'haciendo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return


class TipoX(TipoY):

    def __init__(self):
        super().__init__()
        self.accion = 'creando'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return

    def resolver(self):
        self.accion = 'haciendo algo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return


if __name__ == '__main__':
    y = TipoY()
    y.hacer()
    x = TipoX()
    x.hacer()
    x.resolver()