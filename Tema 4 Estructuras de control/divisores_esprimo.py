
''''
# Dar numero y que dé todos los divisores
numero = float(input("Escribe un número: "))

candidato_divisor = 1
while candidato_divisor <= numero:
    if numero % candidato_divisor == 0:
        print(candidato_divisor)
    candidato_divisor += 1

print("FIN")

'''

########################################### Usando for

numero = int(input("Escribe un número: "))

cantidad_divisores = 0
for candidato_divisor in range(1, numero + 1):
    if numero % candidato_divisor == 0:
        #print(candidato_divisor)
        cantidad_divisores += 1

es_primo = cantidad_divisores == 2

print(f'El número {numero} tiene {cantidad_divisores} divisores')


if es_primo:
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')



################################### Mostrar primos entre 1 y N

N = int(input("N? "))

for numero in range(1, N):
    # Comprobar si número es primo
    cantidad_divisores = 0
    for candidato_divisor in range(1, numero + 1):
        if numero % candidato_divisor == 0:
            cantidad_divisores += 1

    es_primo = cantidad_divisores == 2                  ### ??
if es_primo:
    print("Es primo")


