from unittest import TestCase
from PatronesGRASP.presupuesto.entidades.gasto import Gasto, GastoOtraMoneda
from PatronesGRASP.presupuesto.entidades.meses import Meses
from PatronesGRASP.presupuesto.entidades.linea_presupuesto import LineaPresupuesto


class TestLineaPresupuesto(TestCase):

    def setUp(self) -> None:
        self._linea_presupuesto = LineaPresupuesto("Licencias Sistema 1")
        gasto = Gasto(1200)
        for mes in Meses().meses:
            self._linea_presupuesto.presupuestar_mes(mes, gasto)

    def test_obtener_presupuesto_mes(self):
        gasto = self._linea_presupuesto.obtener_presupuesto_mes('Enero')
        self.assertEqual(gasto.cantidad, 1200)

    def test_obtener_presupuesto_linea(self):
        self.assertEqual(self._linea_presupuesto.obtener_presupuesto_linea(), 14400)

    def test_obtener_gasto_anual(self):
        for mes in self._linea_presupuesto.obtener_gasto_meses():
            print(mes.mes + ':' + str(mes.gasto))


class TestLineaPresupuestolOtraMoneda(TestCase):

    def setUp(self) -> None:
        self._linea_presupuesto = LineaPresupuesto("Licencias Sistema 2")
        gasto1 = GastoOtraMoneda(100, 'U$S')
        gasto1.tipo_de_cambio = 80
        self._linea_presupuesto.presupuestar_mes('Enero', gasto1)
        gasto2 = GastoOtraMoneda(100, 'U$S')
        gasto2.tipo_de_cambio = 82
        self._linea_presupuesto.presupuestar_mes('Febrero', gasto2)
        gasto3 = GastoOtraMoneda(100, 'U$S')
        gasto3.tipo_de_cambio = 84
        self._linea_presupuesto.presupuestar_mes('Marzo', gasto3)
        gasto4 = GastoOtraMoneda(100, 'U$S')
        gasto4.tipo_de_cambio = 86
        self._linea_presupuesto.presupuestar_mes('Abril', gasto4)
        gasto5 = GastoOtraMoneda(100, 'U$S')
        gasto5.tipo_de_cambio = 88
        self._linea_presupuesto.presupuestar_mes('Mayo', gasto5)
        gasto6 = GastoOtraMoneda(100, 'U$S')
        gasto6.tipo_de_cambio = 90
        self._linea_presupuesto.presupuestar_mes('Junio', gasto6)

    def test_obtener_presupuesto_mes(self):
        gasto = self._linea_presupuesto.obtener_presupuesto_mes('Enero')
        self.assertEqual(gasto.cantidad, 8000)

    def test_obtener_presupuesto_linea(self):
        self.assertEqual(self._linea_presupuesto.obtener_presupuesto_linea(), 51000)

    def test_obtener_gasto_anual(self):
        for mes in self._linea_presupuesto.obtener_gasto_meses():
            print(mes.mes + ':' + str(mes.gasto))