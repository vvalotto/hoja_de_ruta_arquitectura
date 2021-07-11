import unittest
from PatronesGRASP.clases.persona import *
from datetime import date


class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        nombre = Nombre("Alejo Antonio", "Valotto")
        documento = Identificacion("DNI", "49330400")
        fecha_de_nacimiento = date(2009, 4, 23)
        self._una_persona = Persona(nombre, documento, fecha_de_nacimiento, "M")

    def test_nombres(self):
        self.assertEqual(str(self._una_persona.nombre), "Alejo Antonio Valotto")

    def test_apellido(self):
        self.assertEqual(self._una_persona.apellido, "Valotto")

    def test_fecha_de_nacimiento(self):
        self.assertEqual(str(self._una_persona.fecha_de_nacimiento), "2009-04-23")

    def test_genero(self):
        self.assertEqual(self._una_persona.genero, "M")

    def test_documento(self):
        self.assertEqual(str(self._una_persona.documento), "DNI:49330400")

    def test_nombre_y_apellido(self):
        self.assertEqual(self._una_persona.apellidos_y_nombres, "Valotto, Alejo Antonio")

    def test_edad(self):
        self.assertEqual(self._una_persona.edad, 12)

    def test_persona(self):
        self.assertEqual(str(self._una_persona), "Alejo Antonio Valotto")


if __name__ == '__main__':
    unittest.main()