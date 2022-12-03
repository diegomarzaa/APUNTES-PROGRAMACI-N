
# MIRAR SI NUMERO ES PAR
numero = int(input("Numero: "))
es_par = numero % 2 == 0
# if (es_par == True):  ------- es redundante
if es_par:
    print("Es par")
else:
    print("Es impar")

#####################################################################################

# Comprovar si n1 es múltiplo de n2
n1 = input("n1: ")
n2 = input("n2: ")

esMúltiplo = n1 % n2 == 0
print(esMúltiplo)

#####################################################################################

# mes comprendido entre 1 y 12
mes = input("mes: ")
print(mes >= 1 and mes <= 12)

#####################################################################################

# comprovar si una nota es valida
esvalida = nota >= 0 and nota <= 10
# no es nota válida
not(esvalida)
#reescribe
noesvalida = nota < 0 or nota > 10

#####################################################################################

# mes (1 y 12) cuando el mes tenga 30 dias
# meses de 30 dias: 4, 6, 9, 11
mes == 4 or mes == 6 or mes == 9 or mes == 11

#####################################################################################

# a, b y c (lados triángulo)                                    EJ. LABORATORIO
# es un triangulo equilatero, isosceles o escaleno??
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if (a == b and b == c):                                            # Poner los ==, a veces pongo solo el =
    print("Equilatero")
# elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):  ---------  se puede simplificar, hay cosas innecesarias
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Escaleno")

#####################################################################################

# Calcular mayor valor de 2 variables
n1 = input("n1: ")
n2 = input("n2: ")

if n1 > n2:
    mayor = n1
elif n2 > n1:
    mayor = n2
print("El mayor es: ", mayor)

##################################################################################### Secuencia while
suma = 0
nota = 0
cantidad = 0

nota = float(input('Nota? '))
while nota >= 0 and nota <= 10:
    nota = float(input('Nota? '))
    suma += nota
    cantidad += 1