palabra1_usuario = input("Dime una palabra: (Palabra 1)")
palabra2_usuario = input("Dime una palabra: (Palabra 1)")


if palabra1_usuario[-3:] == palabra2_usuario[-3:]:
       rima = "Tus palabras riman una barbaridad"
elif palabra1_usuario[-2:] == palabra2_usuario[-2:]:
       rima = "Tus palabras riman un poco"
else:
       rima = "Tus palabras no riman nada"
       

def respuesta(palabra1_usuario,palabra2_usuario,rima):
    print("Ripios")
    print("Su primera palabra: ",palabra1_usuario)
    print("Su segunda palabra: ",palabra2_usuario)
    print(rima)

def main(palabra1_usuario,palabra2_usuario,rima):
        respuesta(palabra1_usuario,palabra2_usuario,rima)

if __name__ == "__main__":
        main(palabra1_usuario,palabra2_usuario,rima)