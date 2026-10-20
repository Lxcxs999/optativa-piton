palabra = input("Dame una palabra: ")

palabra = palabra.lower()

letras = {}


for letra in palabra:
    letras[letra]=palabra.count(letra)
    print()
