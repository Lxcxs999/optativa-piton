edad = int(input("Introduce tu edad: "))
dia = input("Introduce el dia de la semana: ")
sesion_3d = input("¿La sesion es 3D? (si/no): ")

dia_sin_espacios = dia.replace(" ", "")
dia_minusculas = dia_sin_espacios.lower()
sesion_sin_espacios = sesion_3d.replace(" ", "")
sesion_minusculas = sesion_sin_espacios.lower()

if edad < 0:
    print("La edad no es valida")
else:
    if edad < 12:
        precio = 5
    elif edad >= 65:
        precio = 6
    else:
        precio = 8
    print("Precio de la entrada:", precio, "euros")
    if dia_minusculas == "miercoles":
        precio -= 1
        print("Descuento de miercoles: -1 euro")
    if sesion_minusculas == "si":
        precio += 2
        print("Suplemento 3D: +2 euros")
        
    print("Precio final:", precio, "euros")