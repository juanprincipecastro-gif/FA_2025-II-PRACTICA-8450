g = input("genere una contraseña")

print("------------------------")
print("-- valida tu contraseña --")
print("--                      --")
print("-- valida tu contraseña --")
print("      1.ud tiene 3 intentos ")
print("---------------------------")


intentos = 3
while(intentos > 0):
    c = input ("ingrese la contraseña: ")

    if g == c:
        print("\nAcceso concedido Binevenido al Sistema ")
        break
    else:
        intentos-=1
        print("contraseña incorrecta. intentos restantes ", intentos)
else: print("acceso denegado! cerrando sistema ")

