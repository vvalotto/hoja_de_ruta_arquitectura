from abc import ABCMeta, abstractmethod


class BaseAuditor(metaclass=ABCMeta):

    @abstractmethod
    def auditar(self, entidad, auditoria):
        pass