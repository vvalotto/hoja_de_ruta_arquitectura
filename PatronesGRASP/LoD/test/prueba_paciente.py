from entidades.paciente import *
from datetime import date, datetime

una_paciente = Paciente()
una_paciente.nombres = 'Alejo Antonio'
una_paciente.apellido = 'Valotto'
una_paciente.fecha_de_nacimiento = date(2009, 4, 23)
una_paciente.obra_social_nombre = "OSUNER"
una_paciente.obra_social_id = 1

print(una_paciente.nombre_y_apellido)
print(una_paciente.fecha_de_nacimiento)
print(una_paciente.edad)
print(una_paciente.obra_social_nombre)
print(una_paciente.obra_social_id)