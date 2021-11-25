#2.	Elabore una función que tome 
# como argumento tres números enteros y devuelva el mayor

a=int(input("ingresar numero: "))
b=int(input("ingresar numero: "))
c=int(input("ingresar numero: "))

def mayor(a,b,c):
    if((a>b)and(a>c)):
        return a
    if((b>a)and(b>c)):
        return a    
    if((c>a)and(c>b)):
        return c
print (mayor(a,b,c))            