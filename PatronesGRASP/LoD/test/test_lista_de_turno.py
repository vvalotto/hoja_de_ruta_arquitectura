from unittest import TestCase
from LoD.entidades.turno import ListaDeTurnos
from test.ejemplo_turno import fabricar_turno, fabricar_turno_2, fabricar_turno_3


class TestListaDeTurnos(TestCase):

    def setUp(self) -> None:
        self._turno = fabricar_turno()
        self._lista_de_turnos = ListaDeTurnos()

    def test_lista_vacia(self):
        self.assertEqual(len(self._lista_de_turnos.lista), 0)

    def test_agregar_turno(self):
        self._turno = fabricar_turno()
        self._lista_de_turnos.agregar_turno(self._turno)
        self.assertEqual(len(self._lista_de_turnos.lista), 1)

    def test_hay_horario_ocupado(self):
        self.assertEqual(self._lista_de_turnos.hay_horario_ocupado(self._turno.hora), 0)

    def test_eliminar_turno(self):
        self._turno = fabricar_turno()
        self._lista_de_turnos.agregar_turno(self._turno)
        self._lista_de_turnos.eliminar_turno(self._turno)
        self.assertEqual(len(self._lista_de_turnos.lista), 1)

    def test_agregar_nuevo_turno(self):
        self._turno = fabricar_turno()
        self._lista_de_turnos.agregar_turno(self._turno)
        self._turno = fabricar_turno_2()
        self._lista_de_turnos.agregar_turno(self._turno)
        self._turno = fabricar_turno_3()
        self._lista_de_turnos.agregar_turno(self._turno)
        for turno in self._lista_de_turnos.lista:
            print(str(turno.paciente) + " - " + str(turno.hora))
        self.assertEqual(len(self._lista_de_turnos.lista), 3)

    def test_lista_ordenada(self):
        self._turno = fabricar_turno()
        self._lista_de_turnos.agregar_turno(self._turno)
        self._turno = fabricar_turno_2()
        self._lista_de_turnos.agregar_turno(self._turno)
        self._turno = fabricar_turno_3()
        self._lista_de_turnos.agregar_turno(self._turno)
        print(len(self._lista_de_turnos.lista))
        self.assertEqual("15:00:00", str(self._lista_de_turnos.lista[0].hora))
        self.assertEqual("16:00:00", str(self._lista_de_turnos.lista[1].hora))
        self.assertEqual("17:00:00", str(self._lista_de_turnos.lista[2].hora))
