def ejer1(): #creando metodo ejer1
    nombre = input("ingrese su nombre: ")
    carrera = input ("ingrese su carrera: ")

    print(f"\n{nombre}, bienvenido a FA de {carrera}") 

    
def ejer2():
    print("\"\"jesus\"\"")
    
    
    
def ejer3():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y" ))

    print("suma: ", (x+y))
    print("resta: ", (x-y))
    print("multiplicacion: ", (x*y))
    print("division: ", (x/y))


import math #importando la libreria math

def ejer4():
    num = float(input("Ingrese un numero decimal: "))

    print("raiz 2: ", math.sqrt(num))
    print("redondeado: ",round(num,0))
    print("al cubo: ", math.pow(num,3))
    print("raiz 3: ", num ** (1/3))

def ejer5():
    num = input("Ingrese numero: ")

    entero = int (num)
    deci = float(num)

    print("Resto: ", (entero%2))
    print("division:",(deci/3))
