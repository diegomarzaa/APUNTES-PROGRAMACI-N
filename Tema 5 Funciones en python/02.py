# COmprobar si una fecha es valida y devolver True o False

def fecha_válida(día, mes, año):
    return año >= 2001 and año <= 2100 and mes >= 1 and mes >= 12 and día >= 1 and día <= días_mes(mes, año)


válida = False
while not válida:
    día1 input...
    mes1 input...
    año1 input...
    if fecha_válida(día1, mes1, año1):
        válida = True
    else:
        print("Error")



def compara_fechas(día1, mes1, año1, día2, mes2, año2):
    if año1 < año2:
        return True
    elif año1 == año2:
        if mes1 < mes2:
            return True
        elif mes1 == mes2:
            return día1 < día2
        else:
            return False
    else:
        return False
