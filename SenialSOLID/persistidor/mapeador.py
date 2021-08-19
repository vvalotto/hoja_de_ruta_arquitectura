"""
Modulo que convierte o mapea una estructura de objeto python en otra
para persistirlo de acuerdo a almacen definido (archivo plano, xml, BD)
"""
from abc import ABCMeta, abstractmethod


class Mapeador(metaclass=ABCMeta):
    """
    Clase base del mapeo (abracta)
    """
    # Lista los tipo de dato base (fin del proceso recursivo)
    lista_tipos_base = ['int', 'str', 'float', 'None', 'bool', 'date']

    def __init__(self):
        pass

    @staticmethod
    def tipo_dato(tipo, dato):
        """
        Funcion que devuelve un tipo segun la cadena indicada en el parametro tipo
        :param tipo:
        :param dato:
        :return:
        """
        if tipo == 'int':
            return int(dato)
        elif tipo == 'str':
            return str(dato)
        elif tipo == 'float':
            return float(dato)
        elif tipo == 'bool':
            return bool(dato)
        else:
            return None

    @abstractmethod
    def ir_a_persistidor(self, entidad):
        pass

    @abstractmethod
    def venir_desde_persistidor(self, entidad, entidad_mapeada):
        pass


class MapeadorArchivo(Mapeador):
    """
    Implementacion del Mapeo de objetos a un archivo de texto
    """
    def __init__(self):
        super().__init__()
        self._objeto_mapeado = None
        return

    def ir_a_persistidor(self, entidad):
        """
        Mapea la clase a una estructura para persistirla en un archivo.
        La clase es proporcionada por el argumento entidad.
        :param entidad:
        :return:
        """
        atr_lista = []
        # Inicializa la variable de mapeo serializada
        entidad_mapaeada = ''

        # Si es un tipo base mapea solo el valor interno del objeto
        if entidad.__class__.__name__ in Mapeador.lista_tipos_base:
            entidad_mapaeada += str(entidad) + ','
        else:
            # Recorre los miembros que son campos de la clase para el caso de una clase compleja
            # O sea una clase que contiene variables de intancia (campos)
            # Por lo tanto recorre los campos
            # dict = (entidad.__dict__.items())
            for atributo in entidad.__dict__.keys():
                # Si el campo es de tipo de clase base, lo mapea (lo serializa)
                if entidad.__dict__[atributo].__class__.__name__ in Mapeador.lista_tipos_base:
                    entidad_mapaeada += atributo + ':' + str(entidad.__dict__[atributo]) + ','
                else:
                    # Si el clase contiene una coleccion (lista) lo agrega para procesarlo
                    # despues
                    if type(entidad.__dict__[atributo]) is list:
                        atr_lista.append(atributo)
                    else:
                        # Si es un campo que corresponde a una clase compuesta
                        entidad_mapaeada += atributo + ':' + self.ir_a_persistidor(atributo)
            entidad_mapaeada += '\n'

            # Mapeo de los elementos de la coleccin (lista)
            i = 0
            for atributo in atr_lista:
                if type(entidad.__dict__[atributo]) is list:
                    i = 0
                for elemento in entidad.__dict__[atributo]:
                    entidad_mapaeada += atributo + '>' + str(i) + ':' + self.ir_a_persistidor(elemento)
                    i += 1
                    entidad_mapaeada += '\n'
        return entidad_mapaeada

    def venir_desde_persistidor(self, entidad, entidad_mapeada):
        """
        Hace el mapeo desde el almacen de persitencia hacie el objeto
        :param entidad: indica del tipo de objeto que se quiere mapear
        :param entidad_mapeada: la entidad persistida, pero con la estructura con la que persistio
        :return: la entidad requerida con el estructura de objeto
        """
        # separa la lineas del archivo
        sep_registros = entidad_mapeada.split('\n')
        for registro in sep_registros:
            if registro != '':
                # separa cada linea en campos(atributos)
                sep_campos = registro.split(',')
                for campo in sep_campos:
                    # separa cada campo en clave y valor
                    sep_valor = campo.split(':')
                    for atributo in entidad.__dict__.keys():
                        if atributo in sep_valor[0]:
                            if entidad.__dict__[atributo].__class__.__name__ in Mapeador.lista_tipos_base:
                                entidad.__dict__[atributo] = super().tipo_dato(
                                    entidad.__dict__[atributo].__class__.__name__,
                                    sep_valor[1]
                                )
                            elif type(entidad.__dict__[atributo]) is list:
                                entidad.__dict__[atributo].append(float(sep_valor[1]))
        return entidad
