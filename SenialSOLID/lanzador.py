#!/usr/local/bin/python3.4
"""
Programa lanzador del ejemplo
"""

from senial_solid.lector_senial import LectorSenial


class Lanzador:
    """
    Programa Principal
    """
    def __init__(self):
        pass

    @staticmethod
    def ejecutar():
        """
        Ejecucion del programa lanzador
        :return
        """
        senial = LectorSenial(10)

        print("Iniciando")
        print("Paso 1 - Adquiere la señal")
        senial.leer_senial()
        
        print("Paso 2 - Procesa la señal")
        senial.procesar_senial()
        
        print("Paso 3 - Muestra la señal")
        senial.mostrar_senial()
        
        return


if __name__ == "__main__":
    Lanzador().ejecutar()
