import dis

""" SALUDAR """


def saludar(persona):
    print('Hola ' + persona)


print('Ejemplo 1: SALUDAR')
dis.dis(saludar)
print()
# ----------------------

""" SUMA """


def sumar(x, y):
    print(x + y)


print('Ejemplo 1: SUMA')
dis.dis(sumar)
print()
# ----------------------

""" LAZO """


def lazo():
    for i in range(0, 10):
        print(i)


print('Ejemplo 1: LAZO')
dis.dis(lazo)
print()
# ----------------------

""" ELECCION """


def eleccion(opcion):
    if opcion is None:
        print('Nada')
    else:
        print(opcion)


print('Ejemplo 1: ELECCION')
dis.dis(eleccion)
print()
# ----------------------

""" UMBRAL """


def umbral():
    for x in range(0, 5):
        if x > 4:
            y = x + 5
            print(y)


print('Ejemplo 1: UMBRAL')
dis.dis(umbral)
print()
