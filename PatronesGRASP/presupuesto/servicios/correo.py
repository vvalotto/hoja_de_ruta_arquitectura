import smtplib, ssl
from email.mime.text import MIMEText
from PatronesGRASP.presupuesto.servicios.notificador import Notificador
from PatronesGRASP.presupuesto.servicios.credenciales import *


class NotificadorCorreo(Notificador):

    def __init__(self):
        self.__mensajero = 'vvalottotst@gmail.com'
        self.__usuario = usuario
        self.__password = password
        self.__receptores = ['victor.valotto@uner.edu.ar']
        self.__contenido = ''

    def notificar(self, contenido):
        mensaje = MIMEText(contenido, 'html')
        mensaje['Subject'] = 'Validación presupuesto 2'
        mensaje['From'] = self.__mensajero
        mensaje['To'] = ','.join(self.__receptores)

        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(user=self.__usuario, password=self.__password)
        s.sendmail(self.__mensajero, self.__receptores, mensaje.as_string())
        s.quit()