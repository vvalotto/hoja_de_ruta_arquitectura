"""
Ejemplo de violacion del principio de SRP
Aqui la clase LectorSenial tiene todas las responsabilidades del
procesamiento de una senial
"""


class LectorSenial:
    """
    Clase que posee todas las fase del procesamiento de una senial
    1. Lectura de la senial
    2. Procesamiento
    3. Visualizacion de la senial procesada
    """
    def __init__(self, tamanio):
        """
        Inicializa la instancia del lector
        Inicializa la lista de datos a obtener
        Inicializa la lista de datos a procesar
        :param tamanio: numero de valores de la senial a procesar
        """
        self._nro_muestra = tamanio
        self._valores = []
        self._valores_procesados = []
        return
        
    def __leer_dato_entrada(self):
        """
        Metodo privado que se usa para ingresa un solo valor.
        En este caso se ingresa por consola.
        """
        while True:
            try:
                dato = float(input('Valor:'))
                break
            except ValueError:
                print('Dato mal ingresado, <enter>')
        return dato
    
    def leer_senial(self):
        """
        Obtiene la senial de entrada y la guarda en la lista interna
        """
        print("Lectura de la senial")
        for i in range(0, self._nro_muestra):
            print("Dato nro: " + str(i + 1))
            self._valores.append(self.__leer_dato_entrada())
    
    def procesar_senial(self):
        """
        Procesa la senial de manera que para cada valor adquirido se obtenga el doble del mismo
        """
        print("Procesando Senial")
        for i in range(0, self._nro_muestra):
            self._valores_procesados.append(self._valores[i] * 2)
    
    def mostrar_senial(self):
        """
        Muestra la senial procesada en salida de consola
        """
        print("Mostrar la senial")
        for i in range(0, self._nro_muestra):
            print(self._valores_procesados[i])
