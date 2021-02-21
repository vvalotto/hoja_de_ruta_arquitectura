"""

"""

Meses = ['Enero', 'Febrero']


class GastoMensual:

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, valor):
        if valor not in Meses:
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

    def __init__(self, denominacion):
        self._denominacion = denominacion
        self._linea = []
        for mes in Meses:
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