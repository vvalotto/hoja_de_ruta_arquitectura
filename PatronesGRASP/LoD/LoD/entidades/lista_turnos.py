"""

"""


class ListaDeTurnos:

    @property
    def lista(self):
        return self.__lista

    def __init__(self):
        self.__lista = []

    def agregar_turno(self, turno_nuevo):
        self.lista.append(turno_nuevo)
        if len(self.__lista) > 1:
            self.__ordenar_por_horario()

    def eliminar_turno(self, turno):
        if self.hay_horario_ocupado(turno.hora):
            self.__lista.remove(turno)

    def hay_horario_ocupado(self, horario):
        for turno in self.__lista:
            if turno.hora == horario and turno.estado == "ocupado":
                return True
        return False

    def __ordenar_por_horario(self):
        """
        El ordenamiento es sencillo. Como siempre el nuevo turno
        se agrega al final de la lista, este elemento se compara con
        los elementos anteriores hasta que haya uno que sea un horario
        menor al comparado.
        :return:
        """
        # Se toma el ultimo elemento de la lista

        nuevo_turno = self.__lista[len(self.__lista) - 1]
        posicion_a_comparar = self.__lista.index(nuevo_turno)
        # Se recorre la lista de atras para adelante
        for iterador in range(len(self.__lista), 0, -1):

            posicion = iterador - 1
            turno_ocupado = self.__lista[posicion]
            # Si el turno agregado es anterior al turno ya ocupado en el lista
            if nuevo_turno.hora < turno_ocupado.hora:
                # el turno pasa a una la posicion a comparar
                self.__lista[posicion_a_comparar] = turno_ocupado
                posicion_a_comparar = posicion
                self.__lista[posicion] = nuevo_turno
