"""
Instancia de un turno para uso en caso de prueba
"""

from ejemplo_paciente import fabricar_paciente, fabricar_paciente_2, fabricar_paciente_3
from PatronesGRASP.LoD.LoD.entidades.turno import *
from datetime import date, time


def fabricar_turno() -> Turno:
    turno = Turno()
    turno.paciente = fabricar_paciente()
    turno.dia = date(2021, 2, 4)
    turno.hora = time(17, 0, 0, 0)
    return turno


def fabricar_turno_2()-> Turno:
    turno = Turno()
    turno.paciente = fabricar_paciente_2()
    turno.dia = date(2021, 2, 4)
    turno.hora = time(16, 0, 0, 0)
    return turno


def fabricar_turno_3()-> Turno:
    turno = Turno()
    turno.paciente = fabricar_paciente_3()
    turno.dia = date(2021, 2, 4)
    turno.hora = time(15, 0, 0, 0)
    return turno