from unittest import TestCase
from PatronesGRASP.LoD.LoD.aplicacion.gestor_turnos import *
from PatronesGRASP.LoD.test.ejemplo_paciente import *
from datetime import date, time


class TestGestorTurno(TestCase):

    def test_dar_turno(self):
        self._gestor_de_turnos = GestorTurno()
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), date(2021, 7, 16), time(8, 0, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_2(), date(2021, 7, 16), time(12, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_3(), date(2021, 7, 16), time(10, 30, 0))
        self.assertEqual(len(self._gestor_de_turnos.lista_de_turnos), 3)

    def test_notificar_turno(self):
        turnos_avisados = 0
        self._gestor_de_turnos = GestorTurno()
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), date(2021, 7, 16), time(8, 0, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_2(), date(2021, 7, 16), time(12, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_3(), date(2021, 7, 16), time(10, 30, 0))
        self._gestor_de_turnos.notificar_turno(1)
        for turno in self._gestor_de_turnos.lista_de_turnos:
            if turno.aviso == "Avisado": turnos_avisados += 1
        self.assertEqual(turnos_avisados, 3)