
a = int(input('a? '))
b = int(input('b? '))

suma = 0
i = a
while i <= b:
    suma += i
    i += 1


######## OPCION 2
for i in range(10, 21, 1):
    print(i)

######### rangos
list(range(-5, 5, 1))
list(range(10, 0, -1))

#####3
N = 25
for i in range(1, N+1):
    print(i, end=' ')                   ## Reemplazar salto de linea por espacio

####
N = 10
for i in range(0, N):                   ## Lista de n elementos, cada elemento está en la posicion n-1 de la lista
    print(i)


####
a = int(input('a? '))
b = int(input('b? '))

suma = 0
for i in range(a, b+1):
    suma += i
print(suma)

