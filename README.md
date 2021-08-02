# hoja_de_ruta_arquitectura

Demostración de la aplicación de los Principios de Diseño SOLID

S -> SRP: Principio de Responsabiidad Única
O -> OCP: Principio de Abierto/Cerrado
L -> LSP: Principio de Sustitución de Liskov
I -> SIP: Principio de Segregación de Interfases
D -> DIP: Principio de Inversión de Dependencias

Requerimiento 1:
Se desea que se simule el ingreso de una señal por consola, donde cada valor es ingresado por 
este método. La lista de valores ingresados (la señal) debe ser procesada generando una nueva
señal amplificada al doble de la ingresada y posteriormente mostrar el resultado de la señal
amplificada también por consola.

Requerimiento 2:
Es necesario agregar un nuevo tipo de procesamiento ya que hay clientes que necesitan valores de
la señal por debajo de un umbral de valores, que son entregados en un archivo.
Es una nueva versión del Senial_SOLID, pero mantiene la funcionalidad existente.
