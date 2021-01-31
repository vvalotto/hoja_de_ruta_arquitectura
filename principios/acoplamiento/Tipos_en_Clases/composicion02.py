class TipoY:

    def __init__(self):
        self.accion = 'creando'
        print('Tipo Y. Accion: {0}'.format(self.accion))
        return

    def hacer(self):
        self.accion = 'haciendo'
        print('Tipo Y. Accion: {0}'.format(self.accion))
        return


class TipoX:

    def __init__(self, tipo):
        self.accion = 'creando'
        self.tipo = tipo
        print('Tipo X. Accion: {0}'.format(self.accion))
        return

    def resolver(self):
        self.tipo.hacer()
        self.accion = 'haciendo algo'
        print('Tipo X. Accion: {0}'.format(self.accion))
        return


if __name__ == '__main__':
    x = TipoX(TipoY())
    x.resolver()