# Pedir coeficientes
a = float(input('Introduce a: '))
b = float(input('Introduce b: '))

# Calcular y mostrar la solución

if a != 0:
    x = -b / a
    print('x =', x)
else:
    if b == 0:
        print('Infinitas soluciones')
    else:
        print('Error')
