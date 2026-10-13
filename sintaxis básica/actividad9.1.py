precio = float(input("Precio: "))
unidades = int(input("Unidades: "))
porcentaje_descuento = float(input("Descuento (%): "))

subtotal = precio * unidades
descuento = subtotal * porcentaje_descuento / 100
base = subtotal - descuento
iva = base * 0.21
total = base + iva

print(f"Subtotal: {subtotal:.2f} euros")
print(f"Descuento: {descuento:.2f} euros")
print(f"IVA: {iva:.2f} euros")
print(f"Total: {total:.2f} euros")

if total >= 50:
    print("Envio gratuito")
else:
    print("No tiene envio gratuito")
