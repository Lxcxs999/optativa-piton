
numero = int(input("Introduce un número mayor que 1: "))

while numero < 2:
    numero = int(input("Debe ser mayor que 1. Introduce otro número: "))

primo = True
divisor = 2

while divisor < numero and primo:
    if numero % divisor == 0:
        primo = False
    else:
        divisor += 1

if primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")