# def <nombre>(<parametros>):
#    <cuerpo>
#    return <expresion>

def suma(a, b):
    total = a + b
    return total

print(suma(2, 3))

# ARGUMENTOS DE KEYWORD Y VALORES POR DEFECTO

def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_completo('Alejandro', 'Jerez'))
print(nombre_completo('Alejandro', 'Jerez', inverso=True))
print(nombre_completo(apellido='Jerez', nombre='Alejandro'))