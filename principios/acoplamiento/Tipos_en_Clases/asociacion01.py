class TipoX:
    mi_atributo = 'miembro de X'

    def __init__(self):
        print('Tipo X Creado')

    def mostrar_atributos(self, tipo):
        print(self.mi_atributo)
        tipo.hacer()


class TipoY:

    def __init__(self):
        print('Tipo Y Creado')

    @staticmethod
    def hacer():
        print('Tipo Y hace algo')


if __name__ == '__main__':
    tipoX = TipoX()
    tipoY = TipoY()
    tipoX.mostrar_atributos(tipoY)
