"""
Instancia de Paciente para uso en caso de prueba
"""

import datetime
from LoD.Turnero.entidades_basicas.paciente import Paciente
from LoD.Turnero.entidades_basicas.nombre import Nombre
from LoD.Turnero.entidades_basicas.identificacion import Identificacion


def fabricar_paciente() -> Paciente:
    nombre = Nombre("Alejo Antonio", "Valotto")
    documento = Identificacion("DNI", "49330400")
    fecha_de_nacimiento = datetime.date(2009, 4, 23)
    paciente = Paciente(nombre, documento, fecha_de_nacimiento, "M", "OSUNER", 14367839)
    return paciente


def fabricar_paciente_2() -> Paciente:
    nombre = Nombre("Franco Exequiel", "Valotto")
    documento = Identificacion("DNI", "417723200")
    fecha_de_nacimiento = datetime.date(1999, 3, 15)
    paciente = Paciente(nombre, documento, fecha_de_nacimiento, "M", "OSUNER", 14367839)
    return paciente


def fabricar_paciente_3() -> Paciente:
    nombre = Nombre("Victor Octavio", "Valotto")
    documento = Identificacion("DNI", "14367839")
    fecha_de_nacimiento = datetime.date(1962, 8, 6)
    paciente = Paciente(nombre, documento, fecha_de_nacimiento, "M", "OSUNER", 14367839)
    return paciente