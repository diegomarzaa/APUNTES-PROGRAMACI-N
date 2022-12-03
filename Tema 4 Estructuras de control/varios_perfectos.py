número = int(input("N?"))

while número > 0:                                       # No se puede cambiar por for, no se el numero de interaciones
    # Comprobar si cumple la condición pedida
    suma_divisores =0
    for divisor in range(1, número // 2+1):
        if número % divisor == 0:
            suma_divisores += divisor
    es_perfecto = suma_divisores == número

    if es_perfecto:
        print("Es perfecto")
    else:
        print("No es perfecto")

    número = int(input("N?"))
