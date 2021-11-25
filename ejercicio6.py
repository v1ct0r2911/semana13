#6.	Elabore una aplicación en Python 
# que se encargue de imprimir la hora actual 
# en formato de 12 y 24 horas además la fecha actual.

import datetime

def mostrarfecha():
    fecha =datetime.datetime.now()
    print(fecha.strftime("%H:%M:%S"))
    print(fecha.strftime("%Y-%m-%d"))

mostrarfecha()    