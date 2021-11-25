#7.	Elabore una aplicación en Python que se 
# encargue de obtener la fecha y hora local empleando 
# el módulo datetime

from datetime import date, datetime
def test_date():
    hoy=datetime.now()
    print("la fecha actula es: ", hoy)

test_date()