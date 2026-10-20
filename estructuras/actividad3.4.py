
personas = 0
accion = input("Acción (entra, sale o fin): ")

while accion != "fin":
    if accion == "entra":
        if personas < 8:
            personas += 1
        else:
            print("La sala está llena")

    elif accion == "sale":
        if personas > 0:
            personas -= 1
        else:
            print("La sala está vacía")

    print("Aforo actual:", personas)
    accion = input("Acción (entra, sale o fin): ")

print("Control finalizado. Quedan", personas, "personas en la sala")
