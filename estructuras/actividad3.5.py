
IVA = 0.21

precio = float(input("Introduce el precio sin IVA: "))

while precio <= 0:
    print("Precio no válido")
    precio = float(input("Introduce otro precio: "))

importe_iva = precio * IVA
precio_final = precio + importe_iva

print("Precio final con IVA:", precio_final, "euros")