#5.	Elabore una funcion1() y una función2() 
#que sumen y multipliquen respectivamente todos 
#los números de una lista. Por ejemplo:
#  funcion1([1,2,3,4]) debería imprimir 10 y 
# funcion2([1,2,3,4]) debería devolver 24. 

def suma(numeros):
    return sum(numeros)

def multiplicar(numeros):
    x=1
    for i in numeros:
        x*=i
        return x

list=[1,2,3,4,5]
print(suma(list)) 
print(multiplicar(list))       