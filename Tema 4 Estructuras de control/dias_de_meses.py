# Que el dia, mes, año compruebe que es una fecha válida

dia = input("Dia: ")
mes = input("Mes: ")
año = input("Año: ")

es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if mes == 2:
    if es_bisiesto:                  # Año bisiesto
        dias_mes = 29
    else:
        dias_mes = 28
elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
    dias_mes = 30
else:
    dias_mes = 31