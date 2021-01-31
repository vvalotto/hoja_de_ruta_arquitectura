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

    def __init__(self):
        self.accion = 'creando'
        self.tipo = None
        print('Tipo X. Accion: {0}'.format(self.accion))
        return

    def resolver(self):
        self.accion = 'haciendo algo'
        print('Tipo X. Accion: {0}'.format(self.accion))
        return

    def delegar(self):
        self.tipo.hacer()

    def asignar(self, tipo):
        self.tipo = tipo


if __name__ == '__main__':
    x = TipoX()
    x.resolver()
    x.asignar(TipoY())
    x.delegar()