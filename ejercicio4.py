#4.	Elabore una función que lea un 
# carácter y devuelva True si es una 
# vocal, de lo contrario que devuelva False
def vocal1(vocal):
    vocales=["a","e","i","o","u"]
    if vocal in vocales:
        return True
    else:
        return False
vocal=input("ingrese vocal: ")
print(vocal1(vocal))