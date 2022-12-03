cadena = "EJEMPLO"
cadena[3]
# 'M'
cadena[1:5]     # hasta el 4, como los rangos
# 'JEMP'

s1 = "SAL"
s2 = "SALUDO"

s2[0:len(s1)]   # len = 3   # 0:3 = SAL
# 'SAL'
s2[0:len(s1)] == s1
# True

s2[0:len(s2)]   # 0 a 6, en realidad 0 a 5 como rangos
# 'SALUDO'
s2[0:-1]
# 'SALUD'
s2[0:]
# 'SALUDO'
s2[5:]
# 'O'
s2[:5]
# 'SALUD'
s2[:]
# 'SALUDO'
s2[0:len(s2):2]
# "SLD"
s2[::-1]
# 'ODULAS'






for c in "ejemplo"[::-1]:
    print(c)
# o
# l
# p
# m
# e
# j
# e


# ----------------------------------------
# ESCAPES
print("una\ncadena")
# una
# cadena

print("una\tcadena")
# t = tabular

print("una\\ncadena")
# una\ncadena
  
print("Una \"Cosa\" rara.")
# Una "Cosa" rara.

print('a\
b')
# ab
  
print('''Una
cadena 
que ocupa varias
lineas''')
# Una
# cadena
# que ocupa varias
# lineas


# ----------------------------------------
## Longitud, indexación...
a = "Hola"
print(a[0])
# H
print(a[len(a)-1])     #len es 1 menos ya que el indice empieza de 0
# a
print(a[-1])        #ultimo caracter es -1, que confunde ya que el 1r caracter es 0
# a
print(a[-len(a)])
# H
print(a[0:2])
# Ho
print(a[len(a)])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range



# LAS CADENAS SON INMUTABLES
cadena = "Hola"
cadena[0] = "M"   # Error, no se puede modificar una cadena




## Concatenación
for caracter in a:
    print(caracter)
# H
# o
# l
# a

for i in range(len(a)):
    print(a[i])
# H
# o
# l
# a

for i in range(len(a)):
    print(a[len(a)-i-1])
# a
# l
# o
# H

# ----------------------------------------
# LETRA PERTENECE A CADENA
# ----------------------------------------
cadena = "Hola"
letra = "a"
letra in cadena
# True




# ----------------------------------------

cadena = "queda poco, paciencia"

índice = 0
while índice < len(cadena):            # Con <= daria un carácter extra y daria error
    print(cadena[índice])
    índice = índice + 1

for indice in range(len(cadena)):    # for ya le resta 1       # (0, len(cadena), 1)
    print(cadena[índice])


for i in cadena:
    print(i, end=" ")

# ----------------------------------------

# Función contar_paréntesis que recibe una cadena, y devuelve la cantidad de paréntesis que tiene la cadena: ), (
# Ej. "(1 + 2 + 3) = ((4 + 2)))"
# Recorrer todos los caracteres, y comparamos si es parantesis, incrementamos contador

def contar_paréntesis(cadena):
    cantidad = 0                    # contador
    for c in cadena:                # c = cada caracter almacenado en cadena, calcula len(cadena)
        if c == "(" or c == ")":    # si c es parentesis
            cantidad += cantidad    # incrementamos contador
    return cantidad                 # devolvemos contador


# Contar vocales de una cadena de texto y devolver el resultado

def contar_vocales(cadena):
    cantidad = 0                 
    for c in cadena:             
        if c in "aeiou":                # if c == "a" or c == "e" or c == "i" or c == "o" or c == "u"
            cantidad += cantidad
    return cantidad              


# Contar letras mayúsculas de una cadena y devolver el resultado
def contar_mayúsuclas(cadena):
    cantidad = 0                 
    for c in cadena:             
        if c >= "A" and c <= "Z":          # if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            cantidad += cantidad
    return cantidad


# Contar la cantidad de dígitos de una cadena de texto

def contar_digitos(cadena):
    cantidad = 0                 
    for c in cadena:             
        if c >= "0" and c <= "9":          # if c in "0123456789"
            cantidad += cantidad
    return cantidad


# ----------------------------------------
# Funcion que evalue si una cadena contiene un dígito y devuelva True or false

def es_digito(cadena):
    return c >= "0" and c <= "9"

def contar_digitos(cadena):
    cantidad = 0                 
    for indice in range(len(cadena)):             
        if es_digito(cadena[indice]):
            cantidad += 1


def algún_dígito(cadena):
    return contar_digitos(cadena) > 0

def todos_digitos(cadena):
    return contar_digitos(cadena) == len(cadena)
    

def algún_dígito(cadena):           # Cuando encuentre un dígito, que devuelva ya True sin recorrer todos los caracteres
    for caracter in cadena:
        if es_digito(caracter):
            return True
    return False

def algún_dígito_v2(cadena):          # Hace lo mismo, sin usar break, recorre todos los carácteres, la version anterior es más compacta y legible
    creo_que_hay_algun_dígito = False
    indice = 0
    while indice < len(cadena) and not creo_que_hay_algun_dígito:    # Importante el menor estricto, si no, daria error al intentar acceder a un caracter que no existe
        if es_digito(cadena[indice]):
            creo_que_hay_algun_dígito = True
        else:
            indice += 1
    return creo_que_hay_algun_dígito


# Comprobar si se cumple para todos los dígitos

# con return
def todos_digitos(cadena):
    todos = True
    indice = 0
    while indice < len(cadena) and not todos:      # Mientras no haya recorrido todos los caracteres y todos siga siendo cierto
        if not es_digito(cadena[indice]):          # cuando no se cumpla, que se haga falso
            todos = False
        else:
            indice += 1
    return todos

# igual sin return
def todos_digitos(cadena):
    for carácter in cadena:
        if not es_digito(carácter):
            return False
    return True




# Función que recibe una cadena y devuelva si todos los carácteres están ordenados alfabéticamente
def alfabética(cadena):
    for i in range(len(cadena) - 1):
        if cadena[i] > cadena[i + 1]:
            return False
    return True

# al reves
for i in range(len(cadena) -1, -1, -1):
    print(cadena[i])

for i in range(-1, -len(cadena) - 1, -1):
    print(cadena[i])

for i in range(0, len(cadena), 1):
    print(cadena[len(cadena) - 1 - i])





# ------------------------------------------------------------------
# PALINDROMO
# Comprobar si una cadena se lee igual de derecha a izquierda que al revés
# Caracter 0 = len(cadena) - 1 = 8, 1 = 7, 2 = 6...
# len(cadena) = 9

def palindromo(cadena):
    j = len(cadena) - 1
    for i in range(len(cadena)//2):         # Hasta la mitad para que no se repitan las mismas comparaciones otra vez
        if cadena[i] != cadena[len(cadena)-1-i]:           # Ver si no es valido
            return False
        j -= 1
    return True        

cadena = input("Introduce una cadena: ")
while cadena != "":
    if palindromo(cadena):
        print("Es palindromo")
    else:
        print("No es palindromo")
    cadena = input("Introduce otra cadena: ")


# -------------------------------------------------------------------
# SUSTITUIR VOCALES POR PUNTOS

def sustituir_vocales_por_puntos(cadena):
    for i in range(len(cadena)):
        if cadena[i] in "aeiouAEIOU":
            nueva += "."
        else:
            nueva += cadena[i]

cadena = input("Introduce una cadena: ")
print(sustituir_vocales_por_puntos(cadena))



# -------------------------------------------------------------------
# MIRAR SI S1 ES UN PREFIJO DE S2

def es_prefijo(s1, s2):           # Para i [0, len(s1)], que se cumpla que [i] en los dos coinciden
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

print(es_prefijo("sal", "salir"))

# -------------------------------------------------------------------
# V1 PROGRAMA QUE CUENTE LAS PALABRAS DE UNA FRASE

cadena = " un  dos   tres    "
palabras = 0
anterior = " "
for caracter in cadena:
    if caracter != " " and anterior == " ":     # Inicio de palabra
        palabras += 1
    anterior = caracter


# -------------------------------------------------------------------
# PROGRAMA DE CONVERSIÓNN DE BINARIO A DECIMAL

bits = "100101"

n = len(bits)
valor = 0
for bit in bits:
    if bit == "1":
        valor += 2**(n-1)
    n -= 1

print(valor)


























