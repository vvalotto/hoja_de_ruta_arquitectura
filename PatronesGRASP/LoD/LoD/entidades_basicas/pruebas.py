
from identificacion import *
from nombre import *
from persona import Persona

mi_id = Identificacion("DNI", 14367839)
print(mi_id)
print(mi_id.tipo)
print(mi_id.numero)

mi_id2 = Identificacion("Pasaparte", "AADD6890")
print(mi_id2)

mi_nombre = Nombre('victor octavio', 'valotto')
print(mi_nombre.apellidos_y_nombres())


una_persona = Persona(mi_nombre, mi_id, '08/06/1962,', 'M')
print(una_persona)