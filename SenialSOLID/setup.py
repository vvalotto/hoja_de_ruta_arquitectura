from setuptools import setup

setup(
    name='SenialSOLID',
    version='2.1.0',
    description='SenialSOLID: Aplicacion de l Principio SRP',
    author='VV',
    author_email='vvalotto@gmail.com',
    packages=['senial_solid'],
    py_modules=['lanzador'],
    entry_point={'console_scripts':
                 'lanzador = lanzador:Lanzador.ejecutar'}
)

