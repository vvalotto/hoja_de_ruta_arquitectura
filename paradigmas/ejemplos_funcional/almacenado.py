import pickle
import json


def guardar_en_pickle(objeto, nombre_archivo):
    archivo = open(nombre_archivo, 'wb')
    pickle.dump(objeto, archivo)
    archivo.close()


def guardar_en_json(objeto, nombre_archivo):
    objeto_json = json.dumps(objeto)
    nombre_archivo = open(nombre_archivo, 'w')
    nombre_archivo.write(objeto_json)
    nombre_archivo.close()


def fabricar(tipo):
    func = None
    if tipo == 'p':
        func = guardar_en_pickle
    elif tipo == 'j':
        func = guardar_en_json
    return func


def guardar(objeto, nombre_archivo, funcion_guardar):
    funcion_guardar(objeto, nombre_archivo)


analisis_texto = {'texto': 'holasss'}
guardar(analisis_texto, 'hola.txt', fabricar('j'))
