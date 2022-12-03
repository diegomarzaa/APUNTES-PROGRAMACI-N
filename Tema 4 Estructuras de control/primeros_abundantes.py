# Mostrar los N primeros números que cumplen una condición

n = int(input("N?"))
numero = 1
cantidad_abundantes = 0

while cantidad_abundantes < n:

    suma_divisores = 0
    for divisor in range(1, numero // 2 + 1):
        if numero % divisor == 0:
            suma_divisores += divisor

    es_abundante = numero < suma_divisores

    if es_abundante:
        print(numero, end = ' ')
        cantidad_abundantes += 1

    numero += 1




