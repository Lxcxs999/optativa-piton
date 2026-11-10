
numeros = []

num1 = int(input("Dime numero 1: "))
numeros.append(num1)

num2 = int(input("Dime numero 2: "))
numeros.append(num2)

num3 = int(input("Dime numero 3: "))
numeros.append(num3)

mayor = max(numeros)
print(mayor, "es el numero mayor")
numeros.remove(mayor)

menor = min(numeros)
print(menor, "es el numero pequeño")
numeros.remove(menor)

print(numeros[0], "es el numero mediano")