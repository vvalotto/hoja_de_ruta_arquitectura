

class Meses:

    @property
    def meses(self):
        return self.__meses

    def __init__(self):
        self.__meses = ['Enero', 'Febrero',
                        'Marzo', 'Abril',
                        'Mayo', 'Junio',
                        'Julio', 'Agosto',
                        'Setiembre', 'Octubre',
                        'Noviembre', 'Diciembre']
