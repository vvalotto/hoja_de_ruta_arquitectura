from unittest import TestCase
from entidades.linea_prespuesto import *


class TestLineaPresupuesto(TestCase):

    def setUp(self) -> None:
        self._linea_presupuesto = LineaPresupuesto("Licencias Sistema 1")
        self._linea_presupuesto.presupuestar_mes('Enero', 50)
        print(self._linea_presupuesto.denominacion)

    def test_obtener_presupuesto_mes(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100)
        gasto = self._linea_presupuesto.obtener_presupuesto_mes('Enero')
        self.assertEqual(gasto, 100)

    def test_obtener_presupuesto_linea(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100)
        self._linea_presupuesto.presupuestar_mes('Febrero', 200)
        self.assertEqual(self._linea_presupuesto.obtener_presupuesto_linea(), 300)


class TestLineaPresupuestolOtraMoneda(TestCase):

    def setUp(self) -> None:
        self._linea_presupuesto = LineaPresupuestoOtrasMonedas("Licencias Sistema 2", 'Dolar')
        self._linea_presupuesto.presupuestar_mes('Enero', 50, 90)
        print(self._linea_presupuesto.denominacion)

    def test_obtener_presupuesto_mes(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100, 95)
        gasto = self._linea_presupuesto.obtener_presupuesto_mes('Enero')
        self.assertEqual(gasto, 9500)

    def test_obtener_presupuesto_linea(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100, 90)
        self._linea_presupuesto.presupuestar_mes('Febrero', 200, 95)
        self.assertEqual(self._linea_presupuesto.obtener_presupuesto_linea(), 28000)
