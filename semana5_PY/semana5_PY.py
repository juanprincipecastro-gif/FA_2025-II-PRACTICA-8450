def ejer1():
    edad = int(input("ingrese su edad "))

    if edad >= 18:
        print("puede votar.")

        if edad >=25:
            print("candidato para un cargo politico")
        else:
            print("no es candidato para un cargo politico")

    else:
        print("no puede votar.")
        print("no puede ejercer un cargo politico.")

def ejer2():
    lado1 = int(input("ingrese lado1: "))
    lado2 = int(input("ingrese lado2: "))
    lado3 = int(input("ingrese lado3: "))

    if lado1 == lad2 or lado1 == lado3 or lado2 ==lado3:
        print("isosceles")
        
    else:
        print("escaleno")
    ejer2()
