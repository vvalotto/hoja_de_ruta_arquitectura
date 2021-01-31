
class TipoX:

    def __init__(self, id):
        self._id = id
        print('Tipo X Creado', str(self._id))

    def hacer(self):
        print('Tipo X hace algo')
        return


class TipoY:

    def __init__(self):
        self._lista_tipoX = None

    def llenar_lista(self, lista):
        self._lista_tipoX = lista

    def mostrar_lista(self):
        for i in self._lista_tipoX:
            print(i._id)


class TipoZ:

    def __init__(self, lista):
        self._lista_tipoX = lista

    def llenar_lista(self, lista):
        self._lista_tipoX = lista

    def mostrar_lista(self):
        for i in self._lista_tipoX:
            print(i._id)


if __name__ == '__main__':

    lista = []
    lista.append(TipoX(1))
    lista.append(TipoX(2))
    lista.append(TipoX(3))

    lista_inicial = []
    lista_inicial.append(TipoX('a'))
    lista_inicial.append(TipoX('b'))

    tipo_y = TipoY()
    tipo_z = TipoZ(lista_inicial)
    tipo_y.llenar_lista(lista)
    tipo_y.mostrar_lista()
    tipo_z.mostrar_lista()