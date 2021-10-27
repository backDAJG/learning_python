def enumeracion_exhaustiva():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if(respuesta**2 == objetivo):
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion_de_soluciones():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        # print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        # print(f'bajo={bajo} alto={alto} respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

def run(reload=False):
    print("1.) Enumeracion exhaustiva.")
    print("2.) aproximacion de soluciones.")
    print("3.) Busqueda binaria.")
    if reload:
        print("Ecoge una opcion valida.")

    algoritmo = int(input('Escoge el algoritmo que deseas probar: '))

    if algoritmo == 1:
        enumeracion_exhaustiva()
    elif algoritmo == 2:
        aproximacion_de_soluciones()
    elif algoritmo == 3:
        busqueda_binaria()
    else:
        run(reload=True)

run()