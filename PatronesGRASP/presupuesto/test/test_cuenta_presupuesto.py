from unittest import TestCase
from PatronesGRASP.presupuesto.entidades.cuenta_presupuesto import CuentaPresupuesto
from PatronesGRASP.presupuesto.entidades.gasto import Gasto


class TestCuentaPresupuesto(TestCase):

    def setUp(self) -> None:
        self._cuenta = CuentaPresupuesto('10001', 'Servicios Tecnologicos')

    def test_crear_linea(self):
        self._cuenta.crear_linea('Mant1')
        self._cuenta.crear_linea('Lic1')
        self.assertEqual(len(self._cuenta.obtener_lineas_presupuesto()), 2)

    def test_obtener_linea_denominacion(self):
        self._cuenta.crear_linea('Mant1')
        linea = self._cuenta.obtener_linea('Mant1')
        self.assertEqual(linea.denominacion, 'Mant1')

    def test_obtener_linea_presupuesto(self):
        self._cuenta.crear_linea('Mant1')
        linea = self._cuenta.obtener_linea('Mant1')
        self.assertEqual(linea.obtener_presupuesto_linea(), 0)

    def test_actualizar_linea_presupuesto(self):
        self._cuenta.crear_linea('Mant1')
        linea = self._cuenta.obtener_linea('Mant1')
        linea.presupuestar_mes('Enero', Gasto(100))
        self._cuenta.actualizar_linea(linea)
        linea_actualizada = self._cuenta.obtener_linea('Mant1')
        self.assertEqual(linea_actualizada.obtener_presupuesto_linea(), 100)

    def test_eliminar_linea(self):
        self._cuenta.crear_linea('Mant1')
        self._cuenta.crear_linea('Lic1')
        linea = self._cuenta.obtener_linea('Mant1')
        self._cuenta.eliminar_linea(linea.denominacion)
        self.assertEqual(len(self._cuenta.obtener_lineas_presupuesto()), 1)

    def test_obtener_presupuesto_cuenta_una_linea(self):
        self._cuenta.crear_linea('Mant1')
        linea = self._cuenta.obtener_linea('Mant1')
        linea.presupuestar_mes('Enero', Gasto(100))
        linea.presupuestar_mes('Febrero', Gasto(121))
        self.assertEqual(self._cuenta.obtener_presupuesto_cuenta(), 221)

    def test_obtener_presupuesto_cuenta_dos_lineas(self):
        self._cuenta.crear_linea('Mant1')
        linea1 = self._cuenta.obtener_linea('Mant1')
        linea1.presupuestar_mes('Enero', Gasto(100))
        linea1.presupuestar_mes('Febrero', Gasto(121))
        self._cuenta.actualizar_linea(linea1)
        self._cuenta.crear_linea('Lic1')
        linea2 = self._cuenta.obtener_linea('Lic1')
        linea2.presupuestar_mes('Mayo', Gasto(500))
        linea2.presupuestar_mes('Abril', Gasto(400))
        self._cuenta.actualizar_linea(linea2)
        self.assertEqual(self._cuenta.obtener_presupuesto_cuenta(), 1121)