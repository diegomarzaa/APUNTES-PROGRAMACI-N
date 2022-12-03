# LISTAS
# Las listas son una estructura de datos que nos permite almacenar
# varios valores en una sola variable. Las listas son mutables, es
# decir, podemos modificarlas después de su creación.
# Las listas se crean con corchetes y los elementos se separan con
# comas. Los elementos de una lista pueden ser de cualquier tipo,
# incluso otras listas.

# Ejemplo de lista de enteros:
lista = [1, 2, 3, 4, 5]

# Ejemplo de lista de cadenas:
lista = ["uno", "dos", "tres"]

# Ejemplo de lista con 3 sublistas:
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Las listas pueden contener elementos de cualquier tipo, incluso otras listas.
lista = [2.0, "dos", [3, 4, 5]]

# Longitud de una lista
# La función len() devuelve la longitud de una lista, es decir, el número de elementos que contiene.

# Ejemplo:
lista = [1, 2, 3, 4, 5]
print(len(lista)) # 5

lista = [[1], [1,3]]
# len(lista) = 2

len(list(range(1,10,2)))
    # list(range(1,10,2)) = [1, 3, 5, 7, 9]
    # len(list) = 5

# Acceso a los elementos de una lista (INDEXACION)
# Los elementos de una lista se acceden mediante su índice, 
# que es un número entero que indica la posición del elemento dentro de la lista. 
# El primer elemento de una lista tiene índice 0, el segundo 1, el tercero 2, etc.

# Ejemplo:
lista = [1, 2, 3, 4, 5]
print(lista[0]) # 1
print(lista[1]) # 2
print(lista[-1]) # 5
print(lista[-2]) # 4









# Operadores para listas
# El operador + concatena dos listas, es decir, devuelve una lista que contiene los elementos de ambas listas.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2) # [1, 2, 3, 4, 5, 6]

# El operador * repite los elementos de una lista un número determinado de veces.
lista = [1, 2, 3]
print(lista * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]




# Recorrer una lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Ver si un elemento esta en una lista
lista = [1, 2, 3, 4, 5]
print(3 in lista) # True
print(6 in lista) # False

lista = [[1,3],[1,2]]
print([1,2] in lista)   # True
print(1 in lista)       # False





# Corte de listas
# Una lista puede ser cortada para obtener una sublista.
# Para cortar una lista se utiliza la sintaxis [inicio:fin:pasos].
# El índice inicio indica el primer elemento de la sublista,
# el índice fin indica el primer elemento que no se incluye en la sublista,
# y el índice pasos indica el tamaño del paso que se utiliza para recorrer la lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[0:3]) # [1, 2, 3]
print(lista[3:6]) # [4, 5, 6]
print(lista[6:9]) # [7, 8, 9]
print(lista[0:9:2]) # [1, 3, 5, 7, 9]
print(lista[1:9:2]) # [2, 4, 6, 8]
print(lista[0:9:3]) # [1, 4, 7]
print(lista[2:9:3]) # [3, 6, 9]
print(lista[0:9:4]) # [1, 5, 9]
print(lista[:2])    # [1, 2]
print(lista[-3:])   # [7, 8, 9]
print(lista[-3:-1]) # [7, 8]
print(lista[:-1])   # [1,2,3,4,5,6,7,8]



# Reemplazar elemento
# Para reemplazar un elemento de una lista se utiliza el operador de asignación.
lista = [1, 2, 3, 4, 5]
lista[0] = 10
print(lista) # [10, 2, 3, 4, 5]


# ----------------------------------------
# (COPIAS Y MISMAS LISTAS (COMO UTILIZA PYTHON LA MEMORIA)
A = [10,20,30,0]
B = A       # Se asocia B a A, son la misma lista con 2 nombres distintos
A[-1] = 40
print(A)    # [10, 20, 30, 40]
print(B)    # [10, 20, 30, 40]

# Para copiar la lista:
    # En lugar de  B = A, poner:
B = A[:]
B = A + []
B = A * 1

# A == B -> El contenido es el mismo
# A is B -> Son la misma lista (en memoria)
    # A = [10,20,30]
    # B = A
    # C = A[:]
        # A is B -> True
        # A is C -> False
        # A == B -> True
        # A == C -> True


# ----------------------------------------
# AGREGAR Y BORRAR ELEMENTOS DE UNA LISTA
# ----------------------------------------
# Agregar al final de la lista
A = [1, 2, 3, 4, 5]
A.append(6)     # Usar este mejor, directamente lo añade, mas rapido
A = A + [6]     # Esto hace una copia, gasta mas recursos

print(A) # [1, 2, 3, 4, 5, 6]



# Quitar un elemento de una lista
del A[0]
# Es importante no usar bucles para eliminar elementos de una lista,
# ya que al eliminar un elemento, los índices de los elementos que quedan cambian.

del A[0:3]  # Elimina los elementos en los indices 0, 1 y 2
del A[0:]   # Elimina todos los elementos de la lista
del A[:]    # Elimina todos los elementos de la lista
del A       # Elimina la lista


# ----------------------------------------
# ELEMENTO PERTENECIENTE A UNA LISTA
# ----------------------------------------
# Para saber si un elemento pertenece a una lista se utiliza el operador in.
A = [1, 2, 3, 4, 5]
print(3 in A) # True
print(6 in A) # False

if not 3 in A:
    print("No esta")
else:
    print("Si esta")


if 3 not in A:
    print("No esta")
else:
    print("Si esta")


[2, 3, 4] in [1, 2, 3, 4] # False
[2, 3, 4] in [1, [2, 3, 4], 5] # True



# ----------------------------------------
# Rotar hacia la izquierda una lista (no vacía)
# ----------------------------------------``
# Lista inicial = [10, 20, 30, 40, 50]
# Lista final = [20, 30, 40, 50, 10]
lista = [10, 20, 30, 40, 50]
aux = lista[0]
for i in range(len(lista)-1):
    lista[i] = lista[i+1]
lista[len(lista)-1] = aux

# ----------------------------------------
# Rotar hacia la derecha una lista (no vacía)
# ----------------------------------------
# Lista inicial = [10, 20, 30, 40, 50]
# Lista final = [50, 10, 20, 30, 40]

lista = [10, 20, 30, 40, 50]
aux = lista[len(lista)-1]
for i in range(1, len(lista)+1):
    lista[i] = lista[i-1]
lista[0] = aux


# ----------------------------------------
# INVERTIR LISTAS
# ----------------------------------------
def invertirA(lista):
    nueva = []
    for i in range(len(lista)-1, -1, -1):
        nueva.append(lista[i])

    return nueva

una_lista = [2,4,8,1,3,5]




resultado = invertirA(una_lista)
print(resultado)

# ------

def invertirB(lista):
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[len(lista)-1-i]
        lista[len(lista)-1-i] = aux

    return lista

una_lista = [2,4,8,1,3,5]
# print(invertir(una_lista))  # Da None (esto no)
invertirB(una_lista)
print(una_lista)


# ----------------------------------------
# ORDENAR LISTAS
# ----------------------------------------
def crear_lista():
    lista = []
    numero = input("¿N? ")
    while numero != "":
        lista.append(int(numero))
        numero = input("¿N? ")
    return lista


# def ordenar(lista):
#    ...

lista = crear_lista()
print(f'Lista inicial: {lista}')
ordenar(lista)
print(f'Lista ordenada: {lista}')






# ----------------------------------------
# MAXIMO Y MINIMO DE UNA LISTA DE NOTAS
# ----------------------------------------

#


# BORRAR PARES
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        del lista[i]
    else:
        i += 1

print(lista)

# OTRA VERSION
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(lista)-1 - i, -1, -1):
    if lista[i] % 2 == 0:
        del lista[i]

print(lista)
# BORRAR PARES
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        del lista[i]
    else:
        i += 1

print(lista)

# OTRA VERSION
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(lista)-1 - i, -1, -1):
    if lista[i] % 2 == 0:
        del lista[i]

print(lista)
# BORRAR PARES
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        del lista[i]
    else:
        i += 1

print(lista)

# OTRA VERSION
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(lista)-1 - i, -1, -1):
    if lista[i] % 2 == 0:
        del lista[i]

print(lista)
# BORRAR PARES


# ----------------------------------------
# OLAS DE FRÍO
# ----------------------------------------
# Una ola de frío se define como una secuencia de días consecutivos en los que la temperatura es menor que 0
# lista + + + - - - - + + - - - - - + - - - - - - - 
#                4            5             7

lista = []
n = 4   # Parametro de dias seguidos con los que se considera ola de frio

def contar_olas(lista, n):
    olas = 0
    seguidos = 0    # Aumentar cada vez que la temperatura de un dia sea menor que la del dia anterior
    for dia in range(len(lista)):
        if lista[dia] < 0:
            seguidos += 1
        else:
            if seguidos > n:    # si es una ola de frío
                olas += 1
            seguidos = 0
    if seguidos > n:
        olas += 1
    return olas




# ----------------------------------------
# Algoritmo diferente que cuente las palabras
def hace_algo(cadena):
    # S1
    cantidad = 0
    while i < len(cadena):
        cantidad += 1
        while i < len(cadena) and cadena[i] != " ":
            i += 1
        while i < len(cadena) and cadena[i] == " ":
            i += 1
    return cantidad

# S1
i = 0
while i < len(cadena) and cadena[i] == " ":
    i += 1

# Make a program that reads a list of numbers and returns a list with the square of each one
def square_list(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    return lista
