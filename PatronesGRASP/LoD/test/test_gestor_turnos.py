from unittest import TestCase
from LoD.aplicacion.gestor_turnos import *
from test.ejemplo_paciente import *
from datetime import date, time


class TestGestorTurno(TestCase):

    def setUp(self) -> None:
        '''
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), datetime(2020, 4, 19), datetime.time(15, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_2(), datetime(2020, 4, 19), datetime.time(14, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_3(), datetime(2020, 4, 19), datetime.time(14, 30, 0))
        '''

    def test_dar_turno(self):
        self._gestor_de_turnos = GestorTurno()
        self._gestor_de_turnos.dar_turno(fabricar_paciente(), date(2021, 2, 4), time(8, 0, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_2(), date(2021, 2, 4), time(12, 0, 0))
        self._gestor_de_turnos.dar_turno(fabricar_paciente_3(), date(2021, 2, 4), time(10, 30, 0))
        for turno in self._gestor_de_turnos.lista_de_turnos:
            print(str(turno.paciente) + " > " + str(turno.evento))
        self._gestor_de_turnos.notificar_turno(1)
        self.assertEqual(len(self._gestor_de_turnos.lista_de_turnos), 3)

    def test_notificar_turno(self):

        self.assertEqual(0, 0)
