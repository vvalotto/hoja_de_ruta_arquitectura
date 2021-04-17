"Clase Suscriptora"
import time


class Subject():

    def __init__(self):
        self.observadores = []
        self.tiempo_actual = None

    def registrar_observador(self, observador):
        if observador in self.observadores:
            print(observador, ' ya esta suscripto')
        else:
            self.observadores.append(observador)

    def sacar_observador(self, observador):
        try:
            self.observadores.remove(observador)
        except ValueError:
            print('No existe el observador')

    def notificar_observadores(self):
        self.tiempo_actual = time.time()
        for observador in self.observadores:
            observador.notificar(self.tiempo_actual)
