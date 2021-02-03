"""
Instancia de Paciente para uso en caso de prueba
"""

from LoD.entidades.paciente import *
import datetime


def fabricar_paciente() -> Paciente:
    paciente = Paciente()
    paciente.nombres = "Alejo Antonio"
    paciente.apellido = "Valotto"
    paciente.fecha_de_nacimiento = datetime.date(2009, 4, 23)
    paciente.obra_social_id = 1
    paciente.obra_social_nombre = "OSUNER"
    paciente.telefono = 154444444
    return paciente


def fabricar_paciente_2() -> Paciente:
    paciente = Paciente()
    paciente.nombres = "Franco Exequiel"
    paciente.apellido = "Valotto"
    paciente.fecha_de_nacimiento = datetime.date(1999, 3, 15)
    paciente.obra_social_id = 1
    paciente.obra_social_nombre = "OSUNER"
    paciente.telefono = 153666666
    return paciente


def fabricar_paciente_3() -> Paciente:
    paciente = Paciente()
    paciente.nombres = "Victor Octavio"
    paciente.apellido = "Valotto"
    paciente.fecha_de_nacimiento = datetime.date(1962, 6, 8)
    paciente.obra_social_id = 1
    paciente.obra_social_nombre = "OSUNER"
    paciente.telefono = 154523986
    return paciente