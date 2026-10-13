matriculada = True
autorizacion_especial = False
edad = 17

puede_acceder = (matriculada and edad >= 18) or autorizacion_especial
print(puede_acceder)

edad = 18
puede_acceder = (matriculada and edad >= 18) or autorizacion_especial
print(puede_acceder)
