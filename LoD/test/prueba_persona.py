from datetime import date
from LoD.Turnero.entidades_basicas.persona import Persona
from LoD.Turnero.entidades_basicas.nombre import Nombre
from LoD.Turnero.entidades_basicas.identificacion import Identificacion

mi_nombre = Nombre('Victor Octavio', 'Valotto')
mi_documento = Identificacion('DNI', 14367839)

una_persona = Persona(mi_nombre, mi_documento, date(2009, 4, 23), 'M')

print(una_persona.nombre)
print(una_persona.fecha_de_nacimiento)
