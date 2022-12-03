### COMPROBAR SI UN NUMERO ES PERFECTO LA SUMA DE LOS DIVISORES DE UN NUMERO DA ESE NUMERO
numero = int(input("Numero: "))

# Sumar divisores numero
suma_divisores = 0
for divisor in range (1, numero // 2 + 1):
    if numero % divisor == 0:
        suma_divisores += divisor

es_perfecto = suma_divisores == numero

if es_perfecto:
    print("Perfecto")
else:
    print("No es perfecto")







### CALCULAR TODOS LOS NUMEROS PERFECTOS
numero = int(input("Numero: "))

# Sumar divisores numero
suma_divisores = 0
for divisor in range (1, numero // 2 + 1):
    if numero % divisor == 0:
        suma_divisores += divisor

es_perfecto = suma_divisores == numero

if es_perfecto:
    print("Perfecto")
else:
    print("No es perecto")