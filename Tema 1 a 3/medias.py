nota1 = float(input("Nota 1: "))
notamaxima = nota1
notaminima = nota1

nota2 = float(input("Nota 2: "))
if nota2 > notamaxima:
    notamaxima = nota2
if nota2 < notaminima:
    notaminima = nota2


nota3 = float(input("Nota 3: "))
if nota3 > notamaxima:
    notamaxima = nota3
if nota3 < notaminima:
    notaminima = nota3

nota4 = float(input("Nota 4: "))
if nota4 > notamaxima:
    notamaxima = nota4
if nota4 < notaminima:
    notaminima = nota4

print("La nota media es: ", (nota1+nota2+nota3+nota4)/4)
print("La máxima es: ", notamaxima)
print("La mínima es: ", notaminima)