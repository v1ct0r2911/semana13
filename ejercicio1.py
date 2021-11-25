#1.	Elabore una función que tome como 
# argumento dos números enteros y devuelva el mayor.
def mayor (num1,num2):
    if (num1>num2):
        return num1
    if(num2>num1):
        return num2
print("el numero mayor: ",mayor(10,5))

#lista
list=[1,2,3,4,5,6,7,8,9]
print("el mayor es: ",max(list))