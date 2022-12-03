suma = 0
cantidad = 0
mayor = 0
menor = 10

nota = float(input('Nota? '))
while nota >= 0 and nota <= 10:
    suma += nota                          # suma = suma + nota
    cantidad += 1
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
    nota = float(input('Nota? '))

if cantidad == 0:
    print("No hay notas")
else:
    promedio = suma / cantidad
    print("El promedio de las notas es: ", promedio)
    print("La mayor de las notas es: ", mayor)
    print("La menor de las notas es: ", menor)


# que diga además, el porcentaje de suspensos, aprobados, notables y sobresalientes