from datetime import date
from LoD.Turnero.entidades_basicas.paciente import Paciente
from LoD.Turnero.entidades_basicas.nombre import Nombre
from LoD.Turnero.entidades_basicas.identificacion import Identificacion

nombre_paciente = Nombre('Alejo Antonio', 'Valotto')
documento_paciente = Identificacion('DNI', 49330400)
mi_paciente = Paciente(nombre_paciente, documento_paciente, date(2009, 4, 23), 'M', "OSUNER", 14367839)


print(mi_paciente)
print(mi_paciente.fecha_de_nacimiento)
print(mi_paciente.edad)
print(mi_paciente.obra_social_nombre)
print(mi_paciente.obra_social_id)
print(mi_paciente.documento)