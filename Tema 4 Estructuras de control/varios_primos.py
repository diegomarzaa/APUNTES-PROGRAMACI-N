cantidad_primos = 0
numero = int(input("N? "))

while numero > 0:
    cantidad_divisores = 0
    for candidato_divisor in range(1, numero + 1):
        if numero % candidato_divisor == 0:
            cantidad_divisores += 1
    es_primo = cantidad_divisores == 2

    if es_primo:
        cantidad_primos += 1

    numero = int(input("N? "))

print(f'Hay {cantidad_primos} números primos')
