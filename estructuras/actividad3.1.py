
intentos = 0
autorizado = False

while intentos < 3 and not autorizado:
    codigo = input("Introduce el código: ")

    if codigo == "4826":
        autorizado = True
        print("Acceso autorizado")
    else:
        intentos += 1

        if intentos < 3:
            print("Código incorrecto. Intentos restantes:", 3 - intentos)
        else:
            print("Acceso bloqueado")
