#9.	Elabore una aplicación en Python que imprima
# y cuente los dias domingos en un intervalo de fecha.


from datetime import date, timedelta

def generar_fecha_domingo(agnio):
    fecha=date(agnio,1,1)
    fecha+=timedelta(days=6-fecha.weekday())

    while fecha.year == agnio:
        yield fecha
        fecha += timedelta(days=7)
print("Los dias domingos caen:")

for f in generar_fecha_domingo(2021):
    print(f)