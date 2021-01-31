class TipoX:
    mi_atributo = 'miembro de X'

    @staticmethod
    def mostrar_atributos(tipo):
        print(TipoX.mi_atributo)
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
