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
    
def ejer3():
    n=int(input("ingrese un numero: "))

    print()

    for i in range(1,n+1):
        print(i)

        if i % 2 == 0:
            suma +=i

    print("\nSuma de pares: ",suma)


def ejer4():
    cant = int(input("ingrese la cantidad de numeros: "))
    ceros = pares = inpares = 0
    print()
    for i in range(1, cant+1):
        num = int (input(f"ingrese el numero {i}: "))

        if num ==0:
            ceros +=1 # ceros++
        elif num % 2==0: 
            pares +=1 # pares++
        else:
            impares +=1 #inpar++
    print("\n#ceros: ", ceros)
    print("#pares: ", pares)
    print("#impares: ", impares)
          

