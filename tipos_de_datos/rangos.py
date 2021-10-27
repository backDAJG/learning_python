# range(comienzo, fin, pasos)

mi_rango = range(1, 5)

print(type(mi_rango)) # no inclusivo (no incluye el final)

for i in mi_rango:
    print(i)

mi_rango = range(0, 7, 2)
mi_otro_rango = range(0, 8, 2)

print(mi_rango == mi_otro_rango) # True (Value equality) los valores son iguales

for i in mi_rango:
    print(i)

for i in mi_otro_rango:
    print(i)

print(id(mi_rango))
print(id(mi_otro_rango))

print(mi_rango is mi_otro_rango) # False (Object equality) los objetos son iguales

for i in range(0, 101, 2):
    """
        Generamos toda la secuencia de numero pares del cero al 100
    """
    print(i)

for i in range(1, 100, 2):
    """
        Generamos toda la secuencia de numero inpares del cero al 100
    """
    print(i)