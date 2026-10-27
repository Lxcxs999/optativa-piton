# Mostrar un menu con actividades (ir al cine, salir a comer, visitar un museo, hacer deporte, quedarse en casa)
def menu():
    print("============ACTIVIDADES============")
    print("1. Ir al cine       | 10 euros | 3h")
    print("2. Salir a comer    | 20 euros | 2h")
    print("3. Visitar un museo | 8 euros  | 1h")
    print("4. Hacer deporte    | 0 euros  | 1h")
    print("5. Quedarse en casa | 0 euros  | 3h")
    print("====== 6. Salir del programa ======")

# Cada actividad tiene un tiempo, precio
precios = {
    1:10,
    2:20,
    3:8,
    4:0,
    5:0
    }

tiempo = {
    1:3,
    2:2,
    3:1,
    4:1,
    5:3
}


# Programa recibe tiempo del usuario, dinero del usuario y actividad que quiere hacer
def calculos(tiempo,precios):
    # Usuario indica tiempo que tiene
    tiempo_usuario = int(input("Cuanto tiempo tienes? (horas): "))
    # Usuario indica dinero que tiene
    dinero_usuario = int(input("Cuanto dinero tienes? (euros): "))
    actividad_usuario = 0

    while actividad_usuario != 6:
        # Usuario elige actividad que quiere hacer
        actividad_usuario = int(input("Introduce el numero de la actividad que quieras hacer?: "))

        if precios[actividad_usuario] > dinero_usuario:
            print("No tienes dinero suficiente para esta actividad")
        elif tiempo[actividad_usuario] > tiempo_usuario:
            print("No tienes tiempo suficiente para esta actividad")
        else:
            tiempo_usuario -= tiempo[actividad_usuario]
            dinero_usuario -= precios[actividad_usuario]
            print("Dispones de ",tiempo_usuario," horas y ",dinero_usuario," euros")

# Resumen de las actividades


def main(tiempo,precios):
    menu()
    calculos(tiempo,precios)



if __name__ == "__main__":
    main(tiempo,precios)