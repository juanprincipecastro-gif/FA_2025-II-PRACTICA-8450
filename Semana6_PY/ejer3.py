filas = int (input("ingrese numero de files: "))
columnas = int (input("ingrese numero de columnas: "))
print()

i = 0
while i < filas:
    j=0
    while j < columnas:
        print("*", end=" ")
        j+=1
        print()
        i+=1
    print()
