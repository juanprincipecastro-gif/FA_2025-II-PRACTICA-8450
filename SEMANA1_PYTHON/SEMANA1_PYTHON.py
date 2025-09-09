def ejer1(): #creando metodo ejer1
    nombre = input("ingrese su nombre: ")
    carrera = input ("ingrese su carrera: ")

    print(f"\n{nombre}, bienvenido a FA de {carrera}") 

    def ejer2():
        x = int(input("Ingrese el valor de x: "))
        y = int(input("Ingrese el valor de y" ))

        print("suma: ", (x+y))
        print("resta: ", (x-y))
        print("multiplicacion: ", (x*y))
        print("division: ", (x/y))

        ejer2()
