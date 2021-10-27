mi_lista = [1, 2, 3]

print(mi_lista[0])

print(mi_lista[1:]) #slice

mi_lista.append(4) # Agregar un elemento al inicio de una lista

print(mi_lista)

mi_lista[0] = 'a'

print(mi_lista)

mi_lista.pop() # Eliminar el ultimo elemento de una lista

print(mi_lista)

for elemento in mi_lista:
    print(elemento)

a = [1, 2, 3]
b = a

print(a)
print(b)

print(id(a)) # apuntan al mismo espacio en memoria
print(id(b)) # apuntan al mismo espacio en memoria

c = [a, b]

print(c)

a.append(5)

print(a) # usan la misma direccion en memoria
print(b) # usan la misma direccion en memoria
print(c) # usan la misma direccion en memoria


# Clonacion

"""
    podemos unsar slice() o list()
"""

# Clonacion con funcion list()

ac = [1, 2, 3]

id(a)

bc = ac

c = list(ac)

print(id(a))
print(id(c))

# Clonacion con slice()

dc = a[::]

print(dc)
print(id(dc))


# List comprehension

mi_lista_com = list(range(0, 100))

print(mi_lista_com)

double = [i * 2 for i in mi_lista_com]
print(double)

pares = [i for i in mi_lista_com if i % 2 == 0]

print(pares)