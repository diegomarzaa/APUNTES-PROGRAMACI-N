a = int(input("Dame a:"))
b = int(input("Dame b:"))

cantidad = 0

for número in range(a, b + 1):
    suma_divisores = 0
    for divisor in range(1, número // 2 + 1):
        if número % divisor == 0:          # Divisor propio
            suma_divisores += divisor
    es_perfecto = suma_divisores == número

    if es_perfecto:
        print(número)
        cantidad += 1
print(f'Hay {cantidad} número perfectos entre {a} y {b}')