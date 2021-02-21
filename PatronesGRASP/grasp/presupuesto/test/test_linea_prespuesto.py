from unittest import TestCase
from presupuesto.entidades.linea_prespuesto import *


class TestLineaPresupuesto(TestCase):

    def setUp(self) -> None:
        self._linea_presupuesto = LineaPresupuesto("Licencias Sistema 1")
        self._linea_presupuesto.presupuestar_mes('Enero', 50)
        for gasto_mensual in self._linea_presupuesto.obtener_gasto_meses():
            print(gasto_mensual)

    def test_obtener_presupuesto_mes(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100)
        gasto = self._linea_presupuesto.obtener_presupuesto_mes('Enero')
        self.assertEqual(gasto, 100)

    def test_obtener_presupuesto_linea(self):
        self._linea_presupuesto.presupuestar_mes('Enero', 100)
        self._linea_presupuesto.presupuestar_mes('Febrero', 200)
        self.assertEqual(self._linea_presupuesto.obtener_presupuesto_linea(), 300)