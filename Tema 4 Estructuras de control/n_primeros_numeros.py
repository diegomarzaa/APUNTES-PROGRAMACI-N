# Mostrar los N primeros números que cumplen una condición

n = int(input("N?"))
numero = 1
cantidad_primos = 0

while cantidad_primos < n:
    cantidad_divisores = 0
    for candidato_divisor in range(1, numero + 1):
        if numero % candidato_divisor == 0:
            cantidad_divisores += 1
    es_primo = cantidad_divisores == 2
    if es_primo:
        print(numero)
        cantidad_primos += 1
    numero += 1
