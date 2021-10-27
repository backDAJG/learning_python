mi_dic = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}

print(mi_dic['David'])
print(mi_dic['Erika'])
print(mi_dic['Jaime'])

# mi_dic['Erik'] Error la llave no existe

print(mi_dic.get('Juan', 30))

mi_dic['Jaime'] = 20

print(mi_dic)

mi_dic['Pedro'] = 70

print(mi_dic)

del mi_dic['Jaime']

print(mi_dic)

# iterar un diccionario

for llave in mi_dic.keys():
    print(llave)

for valor in mi_dic.values():
    print(valor)

for elemento in mi_dic.items():
    print(elemento)


print('David' in mi_dic) # True
print('Tom' in mi_dic) # False