# PARA QUE NECESITAMOS CLASES
# Las clases nos permiten agrupar datos y funciones relacionadas
# en un solo lugar, de esta forma podemos crear objetos que
# representen entidades del mundo real, como por ejemplo un
# coche, un perro, un ordenador, etc.

# Representar datos de tipo persona (nos interesa el nombre, DNI y edad)
## Con lo que sabemos:
nombre = "Juan"
dni = "12345678Z"
edad = 19

otro_nombre = "Pedro"
otro_dni = "87654321A"
otra_edad = 20
# No hay nada que relacione las variables, si necesitas 30 personas tendrias que hacer 30 variables, 
# la otra opcion sería hacer listas con la misma longitud, para que todos
# los datos de una persona estén en la misma posición de la lista
nombres = ["Juan", "Pedro", "Ana"]
dnis = ["12345678Z", "87654321A", "12345678A"]
edades = [19, 20, 21]
print(nombres[0], dnis[0], edades[0])
print(nombres[1], dnis[1], edades[1])

# Con funciones
def mostrar_persona(nombre, dni, edad):
    print("Nombre: ", nombre)
    print("DNI: ", dni)
    print("Edad: ", edad)
mostrar_persona("Juan", "12345678Z", 19)
mostrar_persona("Pedro", "87654321A", 20)

for i in range(len(nombres)):
    mostrar_persona(nombres[i], dnis[i], edades[i])


# Problema: agregar por ejemplo un domicilio
# Modificar la funcion mostrar_persona con 4 parametros (pero el codigo principal deja de ser valido, se necesitan pasar 4 argumentos)


# Ordenar las personas por su nombre
for i in range(len(nombres)-1):
    menor = i
    for j in range(i+1, len(nombres)):
        if nombres[j] < nombres[menor]:
            menor = j
    if menor != i:
        # Cambiar lista[i] y lista[menor]
        aux = nombres[i]
        nombres[i] = nombres[menor]
        nombres[menor] = aux

# PROBLEMA: Se cambiaria el orden de la lista nombres pero las de DNIS y edad no cambiarian y se quedarian mal




# ---------------------------------
# Otra opcion con listas
persona1 = ["Juan", "12345678Z", 19]
persona2 = ["Pedro", "87654321A", 20]
persona3 = ["Ana", "12345678A", 21]

def mostrar_persona(persona):
    print("Nombre: ", persona[0])
    print("DNI: ", persona[1])
    print("Edad: ", persona[2])
    # Acordarse de en que posicion de la lista está cada dato

mostrar_persona(persona1)
mostrar_persona(persona2)
mostrar_persona(persona3)

personas = [persona1, persona2, persona3]
# Se pueden agrupar los datos correctamente

############
personas[i][1]
personas[i].dni     # Metodos







# ----------------------------------------  
# Clases
# Una clase es un tipo de dato que permite agrupar datos y funciones relacionadas en un solo lugar
# Las clases se definen con la palabra reservada class

# METODOS
# Los metodos son funciones que se definen dentro de una clase
# Los metodos tienen acceso a los atributos de la clase
# Los metodos se definen con la palabra reservada def

# METODOS ESPECIALES
# __init__ es un metodo especial que se ejecuta cuando se crea un objeto de la clase (metodo constructor)
# __str__ devuelve la cadena a mostrar por pantalla


class Alumno:
    def __init__(self, el_nombre, el_dni):
        self.nombre = el_nombre
        self.__dni = el_dni
        self.nota = None    # Sin calificar

    def __str__(self):
        cadena = f'Nombre: {self.nombre}\nDni: {self.__dni}\nNota: '
        if self.Nota == None:
            cadena += 'Sin calificar'
        else:
            cadena += str(self.nota)
        return cadena
    
    def mostar(self):
        print("Nombre: ", self.nombre)
        print("DNI: ", self.__dni)
        print("Nota: ", self.nota)



# Fuera de la clase Alumnos
un_alumno = Alumno("Pepe", "1234A")

print(un_alumno)
# <__main__.Alumno object at 0x000001F1D1B1B0A0>

print(un_alumno.nombre)
# Pepe

print(un_alumno.dni)
# AttributeError: 'Alumno' object has no attribute 'dni'


class Fecha:
    def __init__(self, dia, mes, año):
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        # Un atributo que comienza por __ solo puede ser accedido desde un metodo de la clase, se dice que es un atributo privado

ana = Alumno("Ana Lopez", "123456789")
nochevieja = Fecha(31, 12, 2012)
tortuga = Turtle() #etc







# ----------------------------------------
# PUNTOS
# ----------------------------------------
# ASIGNACIÓN ENTRE OBJETOS
## Al asignar un objeto a otro se copia su referencia
## Si se modifica el objeto original, se modifica el objeto copiado

### Ejemplo:
# Definir la clase punto
p = Punto(1, 1, 1)
q = p
# p y q apuntan al mismo objeto
r = Punto(1, 1, 1)
# r apunta a un objeto distinto (aunque el contenido coincida)

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'


# COMO FUNCION, ESTÁ FUERA DE LA CLASE
def distancia(pto1, pto2):
    return ((pto1.x - pto2.x)**2 + (pto1.y - pto2.y)**2)**0.5

p = Punto2D(1, 1)
q = Punto2D(100, 150)

dist = distancia(p, q)

# ----------------------------------------
# ----------------------------------------

# Como método de la clase
def distancia(self, otro):
    return ((self.x - otro.x)**2 + (self.y - otro.y)**2)**0.5

dist = p.distancia(q)              # p.distancia(q) es equivalente a distancia(p, q) pero con la ventaja de que se puede usar p.distancia() sin necesidad de pasarle el segundo argumento
#                                  # self es el objeto que llama al metodo, en este caso p (p.distancia(q))

# RESULTADO
class punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def distancia(self, otro):
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2)**0.5


# ASIGNACIÓN ENTRE OBJETOS
## Al asignar un objeto a otro se copia su referencia
## Si se modifica el objeto original, se modifica el objeto copiado
p = Punto(1, 1, 1)
q = p
r = Punto(1, 1, 1)

class Punto:
    def copiar(self):
        return Punto(self.x, self.y, self.z)


# ----------------------------------------
class Alumno:
    def calificar(self, nota):
        self.nota = nota

miguel = Alumno("Miguel", "123456789")
miguel.calificar(9.5)

# ----------------------------------------
def escalar(pto, n):
    pto.x *= n
    pto.y *= n

p = Punto2D(100, 200)
escalar(p, 3)



# ----------------------------------------
# ----------------------------------------

