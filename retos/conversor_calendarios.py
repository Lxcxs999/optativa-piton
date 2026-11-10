ano_usuario = int(input("Dime un año: "))

ano_musulman = (32*ano_usuario + 20526)/32
ano_gregoriano = (32*ano_usuario + 20526)/33

def respuesta():
    print("Convertidor entre calendarios")
    print("El año ", ano_usuario, "del calendario gregoriano es aproximadamente el año ", ano_musulman, "del calendario musulmán.")
    print("El año ", ano_usuario, "del calendario musulmán es aproximadamente el año ", ano_gregoriano, "del calendario gregoriano.")



def main():
    respuesta()


if __name__ == "__main__":
    main()
