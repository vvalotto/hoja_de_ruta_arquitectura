from PatronesGOF.observer.observer_simple.subject import *
from PatronesGOF.observer.observer_simple.observador import *

suspcritor = Subject()

print('Agregando observador del tiempo USA')
observador1 = ObservadorTiempoUSA('obs_tiempo_USA')
suspcritor.registrar_observador(observador1)
suspcritor.notificar_observadores()

time.sleep(2)
print('Agregando observador del tiempo EU')
observador2 = ObservadorTiempoEUT('obs_tiempo_EU')
suspcritor.registrar_observador(observador2)
suspcritor.notificar_observadores()

time.sleep(2)
print('Sacando observador del timepo USA')
suspcritor.sacar_observador(observador1)
suspcritor.notificar_observadores()
