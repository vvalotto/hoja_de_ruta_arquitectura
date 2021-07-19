from unittest import TestCase
from PatronesGRASP.presupuesto.entidades.gasto import Gasto, GastoOtraMoneda


class TestGasto(TestCase):

    def setUp(self) -> None:
        self._gasto = Gasto(100)

    def test_gasto(self):
        self.assertEqual(self._gasto.cantidad, 100)

    def test_moneda(self):
        self.assertEqual(self._gasto.moneda, '$')

    def test_etiqueta_gasto(self):
        self.assertEqual(str(self._gasto), '$ 100')


class TestGastoOtraMoneda(TestCase):

    def setUp(self) -> None:
        self._gasto = GastoOtraMoneda(100, "U$S")
        self._gasto.tipo_de_cambio = 100

    def test_gasto(self):
        self.assertEqual(self._gasto.cantidad, 10000)

    def test_moneda(self):
        self.assertEqual(self._gasto.moneda, 'U$S')

    def test_etiqueta_gasto(self):
        self.assertEqual(str(self._gasto), 'U$S 100')
