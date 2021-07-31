from setuptools import setup

setup(
    name='SenialSOLID',
    version='2.3.0',
    description='SenialSOLID - Paso 3: Aplicacion del Principio SRP - con Modulos compilados separados',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'}
)
