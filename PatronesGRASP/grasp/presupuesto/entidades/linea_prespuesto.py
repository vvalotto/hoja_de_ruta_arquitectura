"""

"""

MESES = ['Enero', 'Febrero',
         'Marzo', 'Abril',
         'Mayo', 'Junio',
         'julio', 'Agosto',
         'Setiembre', 'Octubre',
         'Noviembre', 'Diciembre']


class GastoMensual:
    """
    Gasto Mensual prespuestado.
    Contiene el mes y el valor prespuestado
    """
    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, valor):
        if valor not in MESES:
            raise Exception("Error: Nombre de mes inexistente")
        self._mes = valor

    @property
    def gasto(self):
        return self._gasto

    @gasto.setter
    def gasto(self, valor):
        if valor < 0:
            raise Exception("Error: No se pueden ingresar valores negativos")
        self._gasto = valor

    def __init__(self):
        self._mes = None
        self._gasto = 0

    def __str__(self):
        return self._mes + ":" + str(self._gasto)


class LineaPresupuesto:
    """
    Linea de gasto anual a prespuestar.
    Corresponde a un servicio, licencia, contrado.
    Se especifica por su denominacion que respresenta el gasto
    """
    @property
    def denominacion(self):
        return self._denominacion

    def __init__(self, denominacion):
        self._denominacion = denominacion
        self._linea = []
        for mes in MESES:
            mes_gasto = GastoMensual()
            mes_gasto.mes = mes
            self._linea.append(mes_gasto)

    def presupuestar_mes(self, mes, valor_gasto):
        for gasto_mensual in self._linea:
            if mes == gasto_mensual.mes:
                gasto_mensual.gasto = valor_gasto
                break

    def obtener_presupuesto_mes(self, mes):
        for gasto_mensual in self._linea:
            if mes == gasto_mensual.mes:
                return gasto_mensual.gasto
            else:
                Exception("Error")

    def obtener_presupuesto_linea(self):
        gasto_linea = 0
        for gasto_mensual in self._linea:
            gasto_linea += gasto_mensual.gasto
        return gasto_linea

    def obtener_gasto_meses(self):
        return self._linea
