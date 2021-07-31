"""
Clase que genera la salida y visualizacion del contenido de la señal
"""


class Visualizador:

    @staticmethod
    def mostrar_datos(senial):
        print('Mostrar la senial')
        for i in range(0, senial.obtener_tamanio()):
            print(senial.obtener_valor(i))

