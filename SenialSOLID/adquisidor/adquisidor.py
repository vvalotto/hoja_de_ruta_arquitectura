"""
Modulo que define la clase Adquisidor
"""
from SenialSOLID.modelo.senial import Senial


class Adquisidor:
    """
    Adquisdor de datos simple.
    Lee datos desde la consola
    --> _leer_dato_entrada()
    --> obtener_senial_adquirida()
    --> leer_senial()
    """
    def __init__(self, numero_de_nuestras):
        """ Constructor
        numero de muestras: tinicializa el tamaño de la señal a adquirir
        """
        self._senial = Senial()
        self._nro_muestra = numero_de_nuestras

    @staticmethod
    def _leer_dato_entrada():
        """
        Solicita un solo dato por consola. Valida que sea numero
        :return:
        """
        dato = 0
        while True:
            try:
                dato = float(input('Ingresar Valor:'))
                break
            except ValueError:
                print('Dato mal ingresado, <enter>')
        return dato

    def obtener_senial_adquirida(self):
        """
        Devuelva la señal con valores
        """
        return self._senial

    def leer_senial(self):
        """
        Metodo que llama a la lectura por consola y completa el conjunto de valores
        :return:
        """
        print("Lectura de la senial")
        for i in range(0, self._nro_muestra):
            print("Dato nro:" + str(i))
            self._senial.poner_valor(self._leer_dato_entrada())
