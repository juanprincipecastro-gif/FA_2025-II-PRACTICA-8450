import random


print("***************************************+")
print("*   bienvenido al juego adivinador     *")
print("*                                      *")
print("*   1 adivinar el numero entre 1 y 20  *")
print("*   2 tienes 3 intentos                *")
print("****************************************")

intentos = 3
secreto = random.randint(1,20)

while intentos >0:
    num = int(input("\ningrese numero: "))

    if secreto == num:
        print("\nCorrecto! Adivinaste el numero. ")
    else:
        intentos-=1
        if num < secreto: print(f"\nPista:El numero es mayor. te quedan {intentos}")
        else: print(f"\nPista: El numero es menor. intentos restantes {intentos}")
else: print("\nNo lograste adivinar el numero por bot" , secreto)
    
