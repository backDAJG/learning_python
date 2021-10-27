# contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1 # contador = contador + 1


contador_externo = 0
contador_interno = 0

print('iteracion while bucles indefinidos')

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break  # salir del loop

    contador_externo += 1
    contador_interno = 0


# for <variable> in <iterable>:
#    <expresion>


# En la definición anterior debemos entender <iterable> como una colección de objetos;
# y la <variable> como el elemento específico que se está exponiendo mediante el bucle en
# cada iteración.

frutas = ['manzana', 'pera', 'mango']


print('iteracion for bucles definidos')

for fruta in frutas:
    print(fruta)


# estudiantes = {
#     'mexico': 10,
#     'colombia': 15,
#     'puerto_rico': 4,
# }

# for pais in estudiantes:
#     ...

# for pais in estudiantes.keys():
#     ...

# for numero_de_estudiantes in estudiantes.values():
#     ...

# for pais, numero_de_estudiantes in estudiantes.items():
#     ...