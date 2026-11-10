import math

def menu():
    while True:
        print("CÁLCULO DE ÁREAS")
        print("Elija una figura geométrica:")
        print("a) Triangulo")
        print("b) Círculo")
        figura = input("¿Qué figura quiere calcular? (Escribe T o C)")
        figura = figura.lower()

        if figura != "t" and figura != "c":
            print("Tienes que escribir T o C")
        else:
            break
    return figura


def calculos(figura):
    match figura:
        case "t":
            print("HAS ELEGIDO TRIANGULO")
            try:
                base = float(input("Dame la base del triangulo: "))
                altura = float(input("Dame la altura del triangulo: "))
            except ValueError as error:
                print("Error: ", error)
            else:
                print("Un triángulo de base ",base, " y altura ",altura, " tiene un área de ",(base*altura)/2,)
            finally:
                print("Operacion finalizada")
        case "c":
            print("HAS ELEGIDO CIRCULO")
            try:
                radio = float(input("Dame el radio del circulo: "))
            except ValueError as error:
                print("Error: ", error)
            else:
                print("Un círculo de radio ",radio," tiene un área de ",math.PI*(radio**2))
            finally:
                print("Operacion finalizada")

def main():
    figura = menu()
    calculos(figura)


if __name__ == "__main__":
    main()
    