from datetime import date

mi_nombre = Nombre('Victor Octavio', 'Valotto')
mi_documento = Identificacion('DNI', 14367839)

una_persona = Persona(mi_nombre, mi_documento, date(2009, 4, 23), 'M')

print(una_persona.nombre)
print(una_persona.fecha_de_nacimiento)
