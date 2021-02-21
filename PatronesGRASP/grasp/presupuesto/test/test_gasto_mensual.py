from unittest import TestCase
from presupuesto.entidades.linea_prespuesto import *


class TestGastoMensual(TestCase):

    def setUp(self) -> None:
        self._gasto_mensual = GastoMensual()
        self._gasto_mensual.mes = 'Enero'
        self._gasto_mensual.gasto = 100

    def test_mes(self):
        print(self._gasto_mensual.mes)
        self.assertEqual(self._gasto_mensual.mes, 'Enero')

    def test_gasto(self):
        self.assertEqual(self._gasto_mensual.gasto, 100)



