mi_tupla = ()

print(type(mi_tupla))

mi_tupla = (1, '2', True)

print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[2])

# mi_tupla[0] = 2 Error, no podemos modificar una tupla

mi_tupla = (1)

print(type(mi_tupla)) # Es un entero. Tenemos que añadir una coma al final del dato

mi_tupla = (1,)

print(type(mi_tupla))

mi_otra_tupla = (2, 3, 4)

mi_tupla += mi_otra_tupla # Podemos sumar(concatenar) tuplas

print(mi_tupla)

x, y, z = mi_otra_tupla # desenpaquetando(destructurando) los valores de la tupla

print(x, y, z)

def coordenadas():
    return (5, 4)

coordenada = coordenadas()

print(coordenada)

a, b = coordenadas()

print(a, b)

