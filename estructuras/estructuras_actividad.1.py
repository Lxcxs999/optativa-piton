import random

saldo = random.randint(1,1000)
titular = "Ramon Ramirez"
estado_cuenta = True

def ingresar(ingreso):
    if ingreso <= 0:
        print("El ingreso no es valido")
        return saldo
    else:
        print("[INGRESO REALIZADO] Tu saldo actual es de:", saldo, "euros")
        return ingreso + saldo


def retirar(retirada):
    if retirada > saldo or retirada <= 0:
        print ("La retirada supera el saldo en cuenta o no es un valor valido")
        return saldo
    else:
        print("[RETIRADA REALIZADA] Tu saldo actual es de:", saldo, "euros")
        return saldo - retirada

def abrir_cuenta(estado_cuenta):
    if estado_cuenta:
        print("La cuenta ya existe")
    else:
        print("[CUENTA ABIERTA] Cuenta abierta con exito")

def cerrar_cuenta(saldo, estado_cuenta):
    if saldo == 0:
        print("[CUENTA CERRADA] Cuenta cerrada con exito")
        return False
    else:
        print("No puedes cerrar una cuenta con saldo")
        return estado_cuenta


def consultar(titular, saldo, estado_cuenta):
    print("Titular:", titular)
    print("Saldo:", saldo, "euros")
    print("Estado de la cuenta:", estado_cuenta)


operacion = input("Ingrese la operación desea realizar (ingresar, retirar, abrir cuenta, cerrar cuenta o consultar): ")
operacion_sin_espacios = operacion.replace(" ", "")
operacion_minusculas = operacion_sin_espacios.lower()

match operacion_minusculas:
    case "ingresar":
        ingreso = (int(input("Cantidad que quiere ingresar: ")))
        saldo = ingresar(ingreso)
    case "retirar":
        retirada = (int(input("Cantidad que quiere retirar: ")))
        saldo = retirar(retirada)
    case "abrircuenta":
        abrir_cuenta(estado_cuenta)
    case "cerrarcuenta":
        estado_cuenta = cerrar_cuenta(saldo, estado_cuenta)
    case "consultar":
        consultar(titular, saldo, estado_cuenta)
    case _:
        print("La operacion no existe")

print("Saldo final:", saldo)
print("Estado final de la cuenta:", estado_cuenta)