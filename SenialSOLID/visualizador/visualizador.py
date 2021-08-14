"""
Clase que genera la salida y visualizacion del contenido de la señal
"""


class Visualizador:

    @staticmethod
    def mostrar_datos(senial):
        print('Mostrar la senial' + str(senial.tamanio))
        for i in range(0, senial.tamanio):
            print(senial.obtener_valor(i))

