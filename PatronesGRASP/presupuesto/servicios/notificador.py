"""
Simula las Variaciones Protegidas y Polimorfismo de un Notificador
"""

from abc import ABC, abstractmethod


class Notificador(ABC):

    @abstractmethod
    def notificar(self, mensaje):
        pass


class NotificadorConsola(Notificador):

    def notificar(self, mensaje):
        print(mensaje)


class NotificadorArchivo(Notificador):

    def notificar(self, mensaje):
        try:
            notificacion = open('notificacion_presupuesto.txt', 'w')
            notificacion.write(mensaje)
            notificacion.close()
        except IOError:
            print('Error al grabar la linea')