usuario_1 = input('Nombre primer usuario: ')
edad_usuario_1 = int(input(f'Edad de {usuario_1}: '))
usuario_2 = input('Nombre segundo usuario: ')
edad_usuario_2 = int(input(f'Edad de {usuario_2}: '))

if edad_usuario_1 < edad_usuario_2:
    print(f'{usuario_1} es menor que {usuario_2}')
elif edad_usuario_1 > edad_usuario_2:
    print(f'{usuario_1} es mayor que {usuario_2}')
else:
    print(f'{usuario_1} y {usuario_2} tienen la misma edad')