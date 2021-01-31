

def cuadrado_entero(limite_entero):

    for entero in range(1, limite_entero):
        print(entero * entero)


cuadrado_entero(20)
print(list(map(lambda x: x * x, range(1, 20))))
