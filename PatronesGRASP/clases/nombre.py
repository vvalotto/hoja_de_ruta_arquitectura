class Nombre:

    """
    Propiedades accedidas
    """
    @property
    def nombres(self):
        return self.__nombres

    @property
    def apellidos(self):
        return self.__apellidos

    def __init__(self, nombres='Sin Nombre', apellidos ='Sin Apellido'):
        """
        Creación del objeto valor nombre
        :param nombres:
        :param apellido:
        """
        if nombres is None:
            raise Exception("No hay Mombre")
        if apellidos is None:
            raise Exception("no hay apellidos")

        self.__nombres = nombres
        self.__apellidos = apellidos
        return

    def apellidos_y_nombres(self):
        """
        Se devuelve de la manera apellido y nombre
        :return:
        """
        return str(self.__apellidos + ', ' + self.__nombres)

    def apellidos_y_nombres_en_mayusculas(self):
        """
        Se devuelve de la manera apellido y nombre
        :return:
        """
        return self.__apellidos.upper() + ', ' + self.__nombres.upper()

    def __str__(self):
        return self.__nombres + ' ' + self.__apellidos


