from abc import ABC, abstractmethod


class TipoO(ABC):

    @property
    def dato(self):
        return self._dato

    def __init__(self):
        self._dato = 'inicio'
        self._accion = 'creando padre'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))

    @abstractmethod
    def hacer(self):
        pass


class TipoP(TipoO):

    def __init__(self):
        super().__init__()
        self._accion = 'creando hijo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))

    def hacer(self):
        self._accion = 'haciendo algo'
        print('Tipo {0} > Accion: {1}'.format(self.__class__.__name__, self._accion))


if __name__ == '__main__':
    p = TipoP()
    p.hacer()
    print(p.dato)
