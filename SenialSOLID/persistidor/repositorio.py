import sys
from abc import ABCMeta, abstractmethod
import datetime
import traceback


class BaseRepositorio(metaclass=ABCMeta):
    def _init__(self, contexto):
        self._contexto = contexto
    """
    Define la interfaz para el acceso a la persistencia de datos
    """
    @abstractmethod
    def guardar(self, entidad):
        """
        Persiste la entidad
        """
        pass

    @abstractmethod
    def obtener(self, entidad, id_entidad):
        """
        Rescata la entidad indica por id_entidad
        :param entidad: Tipo de entidad que debe rescatar
        :param id_entidad: identificador unico
        :return: retorna la instancia de la entidad indicada
        """
        pass

    @abstractmethod
    def auditar(self, entidad, auditoria):
        """
        Realiza el registro de auditoria sobre la entidad indicada
        :param entidad:
        :param auditoria:
        :return:
        """
        pass

    @abstractmethod
    def trazar(self, entidad, accion, mensaje):
        """
        Realiza la traza del evento ocurrido sobre la entidad y con el mensaje de traza correspondiente
        :param entidad:
        :param accion:
        :param mensaje:
        :return:
        """
        pass


class RepositorioSenial(BaseRepositorio):
    """
    Definicion del Repositorio de la Entidad Senial
    """
    def __init__(self, ctx):
        """
        Se le asocia el contexto correspondiente
        :param ctx: contexto para persistir la senial
        :return:
        """
        super()._init__(ctx)

    def guardar(self, senial):
        """
        Persiste la entidad senial
        :param senial:
        :return:
        """
        try:
            self._contexto.persistir(senial, senial.id)
        except Exception as ex:
            exc_type, exc_value, exc_tb = sys.exc_info()
            tbe = traceback.TracebackException(
                exc_type, exc_value, exc_tb,
            )
            self.trazar(senial, "guardar", tbe)
            raise ex

    def obtener(self, senial, id_senial):
        try:
            return self._contexto.recuperar(senial, id_senial)
        except Exception:
            msj = 'Error al leer una senial persistada: '
            msj += ' - ID: ' + str(id_senial)
            self.trazar(senial, "obtener", msj)
            raise Exception

    def auditar(self, senial, auditoria):
        nombre = 'auditor.log'
        try:
            with open(nombre, 'a') as auditor:
                auditor.writelines('------->\n')
                auditor.writelines(str(senial) + '\n')
                auditor.writelines(str(datetime.datetime.now()) + '\n')
                auditor.writelines(str(auditoria) + '\n')
        except IOError as eIO:
            raise eIO

    def trazar(self, senial, accion, mensaje):

        nombre = 'logger.log'
        try:
            with open(nombre, 'a') as logger:
                logger.writelines('------->\n')
                logger.writelines('Accion: ' + str(accion))
                logger.writelines(str(senial) + '\n')
                logger.writelines(str(datetime.datetime.now()) + '\n')
                logger.writelines(str(mensaje) + '\n')
        except IOError as eIO:
            raise eIO


class RepositorioUsuario(BaseRepositorio):

    def __init__(self, ctx):
        super()._init__(ctx)

    def guardar(self, usuario):
        try:
            self._contexto.persistir(usuario, usuario.id)
        except Exception:
            raise Exception

    def obtener(self, usuario, id_usuario):
        try:
            return self._contexto.recuperar(usuario, id_usuario)
        except Exception:
            raise Exception

    def auditar(self, entidad, auditoria):
        raise "Auditar, Metodo No implementado"

    def trazar(self, entidad, accion, mensaje):
        raise "Trazar Metodo No Implementado"
