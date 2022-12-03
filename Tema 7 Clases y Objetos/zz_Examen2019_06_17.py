# PROBLEMA 2

class TiempoDeUso:
    def __init__(self, usuario, aplicacion):
        self.usuario = usuario
        self.aplicacion = aplicacion
        self.tiempo = 0

# a)
def añadir(lista, usuario, aplicacion, minutos):
    for i in range(len(lista)):
        if lista[i].usuario == usuario and lista[i].aplicacion == aplicacion:
            lista[i].tiempo += minutos
            return False
    # Si llego aqui es que no existe combinacion usuario-aplicacion
    nuevo = TiempoDeUso(usuario, aplicacion)
    nuevo.tiempo += minutos     # Como el tiempo era 0 al crear un objeto, se puede poner así
    lista.append(nuevo)
    return True

# b) Un procedimiento, borrar, que tenga como parámetros una lista de objetos y el nombre de un usuario y que borre de la lista todos los objetos correspondientes al usuario dado.
def borrar(lista, usuario):
    for i in range(len(lista)-1, -1, -1):
        if lista[i].usuario == usuario:
            del lista[i]

# c) 
def añadir(lista, usuario, minutos):
    total = 0
    for i in range(len(lista)):
        if lista[i].usuario == usuario:
            total += lista[i].tiempo
    return total > minutos


# d)
def bloqueados(lista, limite):
    lista_bloqueados = []
    for i in range(len(lista)):
        if not lista[i].usuario in lista_bloqueados:                # Al ponerlo antes que la funcion te ahorras recursos comprobando si no esta
            if se_debe_bloquear(lista, lista[i].usuario, limite):
                lista_bloqueados.append(lista[i].usuario)
    return lista_bloqueados


    
