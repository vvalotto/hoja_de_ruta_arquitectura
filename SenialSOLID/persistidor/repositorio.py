from abc import ABCMeta, abstractmethod
from SenialSOLID.utilidades.auditor import *
from SenialSOLID.utilidades.trazador import *
import datetime


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


class RepositorioSenial(BaseRepositorio, BaseAuditor, BaseTrazador):
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
            self.auditar(senial, "Antes de hacer la persistencia")
            self._contexto.persistir(senial, senial.id)
            self.auditar(senial,  "Se realizo la persistencia")
        except Exception as ex:
            self.auditar(senial,  "Problema al persistir persistencia")
            self.trazar(senial, "guardar", ex)
            raise ex
        return

    def obtener(self, senial, id_senial):
        """
        Implementa la recuperacion de la entidad (senial)
        :param senial:
        :param id_senial:
        :return:
        """
        try:
            self.auditar(senial,  "Antes de recuperar la senial")
            senial_recuperada = self._contexto.recuperar(senial, id_senial)
            self.auditar(senial,  "Se realizo la recuperacion")
            return senial_recuperada
        except Exception:
            self.auditar(senial,  "Error al recuperar")
            msj = 'Error al leer una senial persistada: '
            msj += ' - ID: ' + str(id_senial)
            self.trazar(senial, "obtener", msj)
            raise Exception

    def auditar(self, senial, auditoria):
        """
        Implementacion de la auditoria de la señal
        :param senial:
        :param auditoria:
        :return:
        """
        nombre = 'auditor_senial.log'
        try:
            with open(nombre, 'a') as auditor:
                auditor.writelines('------->\n')
                auditor.writelines(str(senial) + '\n')
                auditor.writelines(str(datetime.datetime.now()) + '\n')
                auditor.writelines(str(auditoria) + '\n')
        except IOError as eIO:
            raise eIO

    def trazar(self, senial, accion, mensaje):
        """
        Implementacion del registro de eventos de la señal
        :param senial:
        :param accion:
        :param mensaje:
        :return:
        """
        nombre = 'logger_senial.log'
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
        return

    def obtener(self, usuario, id_usuario):
        try:
            return self._contexto.recuperar(usuario, id_usuario)
        except Exception:
            raise Exception
