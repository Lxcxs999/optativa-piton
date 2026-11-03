productos = ["pan", "leche", "huevos"]
precios = [0.85, 1.20, 2.50]   # el precio de productos[0] es precios[0], etc.
carrito = []                   # aquí se guardan los precios de lo que se compra

def mostrar_menu():
    print("1. Añadir")
    print("2. Quitar")
    print("3. Repartir la cuenta")
    print("4. Salir")


def convertir_numero(texto):
    numero = int(texto)
    if numero<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return numero


def anadir(carrito, numero):
    if numero not in [0,1,2]:
        raise IndexError("El producto no existe")
    else:
        ()

def quitar(carrito, numero):
    if numero not in [0,1,2]:
        raise IndexError("El producto no existe")
    else:
        ()


def main():
    opcion = 1
    while opcion !=4:
        mostrar_menu()
        try:
            opcion = convertir_numero(input("Que quieres hacer: "))
        except ValueError as error:
            print("Error: ",error)

        match opcion:
            case 1:
                print("0. Pan")
                print("1. Leche")
                print("2. Huevos")
                try:
                    producto = convertir_numero(input("¿Qué producto quieres añadir?"))
                    anadir(carrito, producto)
                except IndexError as error:
                    print("Error: ",error)