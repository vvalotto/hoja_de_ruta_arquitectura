class Nombre:

    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        return

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor
        return

    def __str__(self):
        return self._nombre + ' ' + self._apellido


class Usuario:

    def __init__(self):
        self._id = 0
        self._usuario = ""
        self._nombre_apellido = ""
        self._clave = ""

    # Propiedades
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nombre_apellido(self):
        return self._nombre_apellido

    @nombre_apellido.setter
    def nombre_apellido(self, valor):
        self._nombre_apellido = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        self._clave = valor

    def __str__(self):
        cadena = ''
        cadena += 'id: ' + str(self._id) + '\n'
        cadena += 'usuario: ' + str(self._usuario) + '\n'
        cadena += 'clave: ' + str(self._clave) + '\n'
        cadena += 'nombre: ' + str(self._nombre_apellido) + '\n'
        return cadena
