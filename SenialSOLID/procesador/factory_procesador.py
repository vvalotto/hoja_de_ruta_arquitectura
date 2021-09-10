from .procesador import *


class FactoryProcesador(object):

    @staticmethod
    def obtener_procesador(tipo_procesador, senial, param):
        try:
            procesador = None
            if tipo_procesador == 'amplificador':
                amplificacion = int(param[0])
                procesador = ProcesadorAmplificador(senial, amplificacion)

            elif tipo_procesador == 'umbral':
                umbral = int(param[0])
                procesador = ProcesadorConUmbral(senial, umbral)

            return procesador
        except Exception as ex:
            raise ex