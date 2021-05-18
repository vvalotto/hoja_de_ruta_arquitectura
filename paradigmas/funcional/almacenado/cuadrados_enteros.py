
print('Funcion Potencia al cuadrado - programación estructurada')


def cuadrado_entero(limite_entero):

    for entero in range(1, limite_entero):
        print(entero * entero)


cuadrado_entero(20)
# ------------------------------

print('Funcion Potencia al cuadrado - programación OO')


class CuadradoEntero:

    def calcular(self, limite_entero):
        for entero in range(0, limite_entero):
            print(entero * entero)


calculo = CuadradoEntero()
calculo.calcular(20)
# ------------------------------

print('Funcion Potencia al cuadrado - programación funcional')

print(list(map(lambda i: i * i, range(1, 20))))
