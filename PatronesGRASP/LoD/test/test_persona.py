import unittest
from LoD.entidades.persona import *
from datetime import date


class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        self._una_persona = Persona()
        self._una_persona.nombres = "Alejo Antonio"
        self._una_persona.apellido = "Valotto"
        self._una_persona.fecha_de_nacimiento = date(2009, 4, 23)

    def test_nombres(self):
        self.assertEqual(self._una_persona.nombres, "Alejo Antonio")

    def test_apellido(self):
        self.assertEqual(self._una_persona.apellido, "Valotto")

    def test_fecha_de_nacimiento(self):
        self.assertEqual(str(self._una_persona.fecha_de_nacimiento), "2009-04-23")

    def test_genero(self):
        self.assertEqual(self._una_persona.genero, None)

    def test_documento(self):
        self.assertEqual(self._una_persona.documento, None)

    def test_nombre_y_apellido(self):
        self.assertEqual(self._una_persona.nombre_y_apellido, "Alejo Antonio Valotto")

    def test_edad(self):
        self.assertEqual(self._una_persona.edad, 11)

    def test_persona(self):
        self.assertEqual(str(self._una_persona), "Alejo Antonio Valotto")


if __name__ == '__main__':
    unittest.main()