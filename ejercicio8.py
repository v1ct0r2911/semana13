#8.	Elabore una aplicación en Python que obtenga 
# la diferencia entre 2 fechas, es decir el número 
# de dias. 

from datetime import date

def diferencia_dias(fecha1, fecha2):
    return (fecha2-fecha1).days

hora=date.today()
navidad=date(2021,12,25)
resultado=diferencia_dias(navidad,hora)

print(resultado)    