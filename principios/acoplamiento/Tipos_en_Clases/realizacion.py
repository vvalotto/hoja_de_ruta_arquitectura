from abc import ABC, abstractmethod


class TipoY(ABC):

    def __init__(self):
        self._dato = 'inicio'
        self.accion = 'creando padre'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return

    @abstractmethod
    def hacer(self):
        pass


class TipoX(TipoY):

    def __init__(self):
        super().__init__()
        self.accion = 'creando hijo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return

    def hacer(self):
        self.accion = 'haciendo algo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self.accion))
        return


if __name__ == '__main__':
    x = TipoX()
    x.hacer()
    print(x._dato)