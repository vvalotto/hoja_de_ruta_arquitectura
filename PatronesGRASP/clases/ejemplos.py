

class Identificacion:

    @property
    def tipo(self):
        return self.__tipo

    @property
    def numero(self):
        return self.__numero

    def __init__(self, tipo, numero):
        self.__tipo = tipo
        self.__numero = numero

    def __str__(self):
        return self.__tipo + ":" + str(self.__numero)


if __name__ == "__main__":
    mi_id = Identificacion("DNI", 14367839)
    print(mi_id)
    print(mi_id.tipo)
    print(mi_id.numero)

    mi_id2 = Identificacion("Pasaparte", "AADD6890")
    print(mi_id2)
