from unittest import TestCase
from LoD.Turnero.entidades.turno import *
from LoD.test.ejemplo_paciente import fabricar_paciente
from datetime import datetime, date, time


class TestTurno(TestCase):

    def setUp(self) -> None:
        self._turno = Turno()
        self._turno.paciente = fabricar_paciente()
        self._turno.dia = date(2020, 4, 18)
        self._turno.hora = time(17, 0, 0, 0)

    def test_dia(self):
        self.assertEqual(str(self._turno.dia), "2020-04-18")

    def test_hora(self):
        self.assertEqual(str(self._turno.hora), "17:00:00")

    def test_paciente(self):
        self.assertEqual(str(self._turno.paciente), "Alejo Antonio Valotto")

    def test_aviso(self):
        self.assertEqual(self._turno.aviso, "sin aviso")

    def test_estado(self):
        self.assertEqual(self._turno.estado, "ocupado")

    def test_evento(self):
        self.assertEqual(self._turno.evento, datetime(2020, 4, 18, 17, 0, 0, 0))
