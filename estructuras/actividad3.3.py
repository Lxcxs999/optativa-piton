
precio = 170
pagado = 0

while pagado < precio:
    moneda = int(input("Introduce una moneda (10, 20, 50 o 100 céntimos): "))

    if moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100:
        pagado += moneda
        print("Total pagado:", pagado, "céntimos")
    else:
        print("Moneda no aceptada")

cambio = pagado - precio

print("Producto entregado")
print("Cambio en céntimos:", cambio)
print("Cambio en euros:", cambio / 100, "€")
