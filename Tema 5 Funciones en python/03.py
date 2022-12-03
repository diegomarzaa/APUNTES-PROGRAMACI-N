def mostrar_al_reves(x): 
    while x > 0:
        print(x % 10)
        x //= 10
    print(f'Dentro x vale {x}')

# Suponemos que numero > 0
def contar_digitos(x):
    digitos = 0
    while x > 0:
        digitos += 1
        x //= 10
    return digitos

# Suponemos que numero > 0
def sumar_digitos(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x //= 10
    return suma


# Programa principal
x = int(input("N? ")) # Suponemos n > 0
mostrar_al_reves(x)

print()
print(f'Fuera x vale {x}')



# Funcion "al_reves" que recibe un x > 0 y lo escribe al revés




#  funcion que a partir de x = flotante y n = entero, calcular X elevado a la N sin usar las operaciones del n:

def elevado(x, n):
    producto = 1
    for i in range(abs(n)):
        producto *= x
    if n < 0:
        producto = 1 / producto
    return producto

# Programa principal
x = float(input("x? "))
n = int(input("n? "))
print(elevado(x, n))

