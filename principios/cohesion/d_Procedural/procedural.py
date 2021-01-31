'''
class Parser(object):

    def leer_archivo(self, archivo):
        return

    def informar_error_lectura(self, error):
        return

    def parsear_linea(self, linea):
        return

    def informar_error_linea(self, error):
        return

    def guardar_entidad(self, entidad):
        return

    def auditar(self, mensaje):
        return


parser_paciente = Parser()
try:
    parser_paciente.leer_archivo('lista.txt')
    while ...
        entidad =  parser_paciente.parsear_linea()
        if entidad is None:
            parser_paciente.informar_error_linea('Error Linea')
        else:
            parser_paciente.guardar_entidad(entidad)
            parser_paciente.auditar('Guardado')
except IOError:
    parser_paciente.informar_error_lectura(IOError)
'''


