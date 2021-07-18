from unittest import TestCase
from PatronesGRASP.grasp.presupuesto.entidades.gasto_mensual import *
from PatronesGRASP.grasp.presupuesto.entidades.gasto import *


class TestGastoMensual(TestCase):

    def setUp(self) -> None:
        self._gasto_mensual = GastoMensual('Enero')
        self._gasto_mensual.gasto = Gasto(100)
        self._gasto_mensual_otra_moneda = GastoMensual('Febrero')
        self._gasto_mensual_otra_moneda.gasto = GastoOtraMoneda(50, 'U$S')
        self._gasto_mensual_otra_moneda.gasto.tipo_de_cambio = 100

    def test_mes(self):
        print(self._gasto_mensual_otra_moneda.mes)
        self.assertEqual(self._gasto_mensual_otra_moneda.mes, 'Febrero')

    def test_gasto(self):
        self.assertEqual(str(self._gasto_mensual_otra_moneda.gasto), 'U$S 50')

    def test_gasto_en_pesos(self):
        self.assertEqual(self._gasto_mensual_otra_moneda.gasto_en_pesos, 5000)
        self.assertEqual(self._gasto_mensual.gasto_en_pesos, 100)


