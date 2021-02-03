"""
Turno
"""

import datetime


class Turno:

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, valor):
        self._dia = valor

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, valor):
        self._hora = valor

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor
        if self._paciente != "" or self._paciente is not None:
            self._estado = "ocupado"
        else:
            self._estado = "vacio"

    @property
    def aviso(self):
        return self._aviso

    @aviso.setter
    def aviso(self, valor):
        self._aviso = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def evento(self):
        evento = datetime.datetime(self._dia.year, self._dia.month, self._dia.day,
                                   self._hora.hour, self._hora.minute, self._hora.second, 0)
        return evento

    def __init__(self):
        self._dia = None
        self._hora = None
        self._paciente = None
        self._aviso = "sin aviso"
        self._estado = "vacio"


class ListaDeTurnos:

    @property
    def lista(self):
        return self._lista

    def __init__(self):
        self._lista = []

    def agregar_turno(self, turno_nuevo):
        self.lista.append(turno_nuevo)
        if len(self._lista) > 1:
            self._ordenar_por_horario()
        return

    def eliminar_turno(self, turno):
        if self.hay_horario_ocupado(turno.hora) > 0:
            self._lista.remove(turno)
        return

    def hay_horario_ocupado(self, horario):
        for turno in self._lista:
            if turno.hora == horario and turno.estado == "ocupado":
                return self._lista.index(turno)
        return 0

    def _ordenar_por_horario(self):
        """
        El ordenamiento es sencillo. Como siempre el nuevo turno
        se agrega al final de la lista, este elemento se compara con
        los elementos anteriores hasta que haya uno que sea un horario
        menor al comparado.
        :return:
        """
        # Se toma el ultimo elemento de la lista

        nuevo_turno = self._lista[len(self._lista) - 1]
        posicion_a_comparar = self._lista.index(nuevo_turno)
        # Se recorre la lista de atras para adelante
        for iterador in range(len(self._lista), 0, -1):

            posicion = iterador - 1
            turno_ocupado = self._lista[posicion]
            # Si el turno agregado es anterior al turno ya ocupado en el lista
            if nuevo_turno.hora < turno_ocupado.hora:
                # el turno pasa a una la posicion a comparar
                self._lista[posicion_a_comparar] = turno_ocupado
                posicion_a_comparar = posicion
                self._lista[posicion] = nuevo_turno
        return
