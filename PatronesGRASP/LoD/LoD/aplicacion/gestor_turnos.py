
from entidades.turno import *
from datetime import timedelta, datetime


class GestorTurno:

    @property
    def lista_de_turnos(self):
        return self._lista_de_turnos.lista

    def __init__(self):
        self._dia_de_turnos = datetime.today()
        self._lista_de_turnos = ListaDeTurnos()

    def dar_turno(self, paciente, dia, hora):
        turno = Turno()
        turno.dia = dia
        turno.hora = hora
        turno.paciente = paciente
        self._lista_de_turnos.agregar_turno(turno)

    def notificar_turno(self, plazo_notificacion):
        for turno in self._lista_de_turnos.lista:
            if turno.evento - timedelta(days=plazo_notificacion) > datetime.today():
                mensaje = "Turno con el doctor: " + str(turno.evento)
                self._enviar_notificacion(turno.paciente, mensaje)

    @staticmethod
    def _enviar_notificacion(paciente, mensaje):
        print("Paciente: " + paciente.nombre_y_apellido)
        print("Al telefono: " + str(paciente.telefono))
        print("Mensaje: " + mensaje)
