while True:
    num = int(input("ingrese un numero(0 salir): "))
    sumap = sumai =0
    if  num<=0:
        print("numero invalido. ingrese nuevamente")
        continue

    if num ==0:
        break

    if num%2 ==0:
         sumap+=num
    else:
        sumai += num
