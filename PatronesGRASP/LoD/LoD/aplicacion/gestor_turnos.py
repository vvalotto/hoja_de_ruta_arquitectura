
from PatronesGRASP.LoD.LoD.entidades.turno import *
from PatronesGRASP.LoD.LoD.entidades.lista_turnos import *
from datetime import timedelta, datetime


class GestorTurno:

    @property
    def lista_de_turnos(self):
        return self.__lista_de_turnos.lista

    def __init__(self):
        self._dia_de_turnos = datetime.today()
        self.__lista_de_turnos = ListaDeTurnos()

    def dar_turno(self, paciente, dia, hora):
        turno = Turno()
        turno.dia = dia
        turno.hora = hora
        turno.paciente = paciente
        self.__lista_de_turnos.agregar_turno(turno)

    def notificar_turno(self, plazo_notificacion):
        for turno in self.__lista_de_turnos.lista:
            print(turno.evento - timedelta(days=plazo_notificacion))
            if turno.evento - timedelta(days=plazo_notificacion) > datetime.today():
                mensaje = "Turno con el doctor: " + str(turno.evento)
                self.__enviar_notificacion(turno.paciente, mensaje)
                turno.aviso = "Avisado"

    def __enviar_notificacion(self, paciente, mensaje):
        print("Paciente: " + paciente.apellidos_y_nombres)
        print("Al telefono: " + str(paciente.telefono))
        print("Mensaje: " + mensaje)
