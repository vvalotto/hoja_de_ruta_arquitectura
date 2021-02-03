from entidades.persona import *
from datetime import date, datetime

una_persona = Persona()
una_persona.nombres = 'Alejo Antonio'
una_persona.apellido = 'Valotto'
una_persona.fecha_de_nacimiento = date(2009, 4, 23)



print(una_persona.nombre_y_apellido)
print(una_persona.fecha_de_nacimiento)
print(str(una_persona))