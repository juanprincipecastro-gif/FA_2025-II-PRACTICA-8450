import math


def ejer1():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:
        print("Menor de edad")
    else:
        if edad >= 18 and edad <=64:
            print("Adulto")
        else:
            print("adulto mayor")

def ejer2():
       annio = int(input("ingrese el año: "))

       if (annio %4 == 0 and annio %100 != 0) or (annio %400 ==0):
           print("el año bisiesto")
       else:
           print("el año no es bisiesto")
       if annio %2 ==0:
           print("el año es par")
       else:
           print("el año es impar")

def ejer3():
    monto = float(input("ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion=int(input("\ningrese una opcion: "))

    match opcion:
        case 1: print("dolares: ", round((monto/3.75),0))
        case 2: print(f"euros: {monto/4.05:.2f}")
        case 3: print("opcion incorrectas")

import math

def ejer4():
    print("Bienvenido al sistema de calculos de areas\n")
    print("1. cuadrado")
    print("2. rectangulo")
    print("3. triangulo")
    print("4. circulo\n")

    opcion = int(input("ingrese una opcion: "))

    match opcion:
        case 1:
            lado = int(input("ingrese lado: "))
            print("area cuadrado: ",lado*lado)
        case 2:
            bse = int(input("ingrese la base: "))
            alt = int(input("ingrese la altura: "))
            print("area rectangulo: ", (bse*alt))
        case 3:
            bse2 = int(input("ingrese la base: "))
            alt2 = int(input("ingrese la altura: "))
            print("area tringulo: ",(bse2*alt2)/2)
        case 4:
            radio = float(input("ingrese el radio: "))
            print("area del circulo: ",(round(math.pi * radio**2),2))
        case _: print("opcion incorrecta")



ejer3()


    


 