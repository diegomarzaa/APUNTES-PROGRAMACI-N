# Para reprensentar una matriz, lista de listas
matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

# Acceso a elementos
## Elemento 10
print(matriz[2][1])

# Crear una matriz filas x columnas MAL
filas = 3
columnas = 4

# ESTO IMPORTANTE NO HACERLO, YA QUE SE COPIA LA REFERENCIA
matriz = [[0] * columnas] * filas

# Crear una matriz filas x columnas BIEN
filas = 3
columnas = 4
matriz = []
for fila in range(filas):
    matriz.append([0] * columnas)

# Hallar dimensiones
filas = len(matriz)         # Cantidad elementos matriz
columnas = len(matriz[0])   # Cantidad elementos fila cualquiera


# ----------------------------------------
# ----------------------------------------


# LEER MATRIZ
for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna] = int(input(f"{fila},{columna}"))

# IMPRIMIR MATRIZ
for fila in range(filas):
    for columna in range(columnas):
        print(matriz[fila][columna], end=" ")
    print()



# ----------------------------------------

# FUNCION QUE RECIBA UNA MATRIZ M Y ROTE A LA IZQUIERDA CADA FILA
def rotarmatriz(M):
    nfilas = len(M)
    ncols = len(M[0])
    for fila in range(nfilas):
        aux = M[fila][0]
        for columna in range(ncols-1):
            M[fila][columna] = M[fila][columna+1]
        M[fila][ncols-1] = aux
    return M

M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
rotarmatriz(M)

# ----------------------------------------
# FUNCION REFLEXION HORIZONTAL
def reflexion_horizontal(M):
    nfilas = len(M)
    ncols = len(M[0])
    nueva = []
    for fila in range(nfilas):
        nueva.append([0] * ncols)
    for fila in range(nfilas):
        for columna in range(ncols):
            nueva[fila][columna] = M[fila][ncols - 1 - columna]
    return nueva

M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(reflexion_horizontal(M))

# FUNCION REFLEXION VERTICAL
#---------------------------

# COMPROBAR SI UNA MATRIZ ES SIMETRICA
def es_simetrica(M):
    nfilas = len(M)
    ncols = len(M[0])
    if nfilas != ncols:
        return False
    for fila in range(nfilas):
        for columna in range(ncols):
            if M[fila][columna] != M[columna][fila]:
                return False
    return True

# 1  2  3
# 0  1  4
# 0  0  1

# ES TRIANGULAR
# comprobar que los elementos de debajo de la diagonal son 0
def es_triangular():
    nfilas = len(M)
    ncols = len(M[0])
    if nfilas != ncols:
        return False
    for fila in range(1, nfilas):
        for columna in range(fila):
            if M[fila][columna] != 0:
                return False
    return True
        


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# HACER LA TRASPUESTA DE UNA MATRIZ, 

def traspuesta(M): 
    nfilas = len(M)
    ncols = len(M[0])
    nueva = []
    nfilasT = ncols
    ncolsT = nfilas
    for fila in range(nfilasT):
        nueva.append([0] * ncolsT)
    for fila in range(nfilas):
        for columna in range(ncols):
            nueva[columna][fila] = M[fila][columna]
    return nueva
# 1  2  3
# 0  1  4
# 3  0  1
# 6  5  2



# ----------------------------------------
# DADA UN ELEMENTO DE UNA MATRIZ, DECIR SI ES VALLE
# es valle si es menor que todos sus vecinos. Explicado paso a paso
def es_valle(M, f, c): # f y c son las coordenadas del elemento a comprobar
    for fila in range(f-1, f+2): # recorre las filas de arriba a abajo
        for columna in range(c-1, c+2): # recorre las columnas de izquierda a derecha
            if (fila != f or columna != c) and M[f][c] >= M[fila][columna]: # si no es el elemento a comprobar y es mayor o igual que alguno de sus vecinos no es valle y devuelve False (no es necesario seguir comprobando) 
                return False
    return True

def contar_valles(m):
    nfilas = len(m)
    ncols = len(m[0])
    contador = 0
    for fila in range(1, nfilas-1):
        for col in range(1, ncols-1):
            if es_valle(m, fila, col):
                contador += 1
    return contador





### FALLOS COMUNES
# - Hacer return de la matriz en una funcion cuando el hecho de modificarla ya modifica la matriz original, no hace falta devolverla


