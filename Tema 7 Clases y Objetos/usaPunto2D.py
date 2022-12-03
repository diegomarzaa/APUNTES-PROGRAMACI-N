from punto2D import punto2D

p = punto2D(10, 20)
q = punto2D(10, 20)
r = p

print(f'p es {p}')
print(f'q es {q}')

print(f' ¿p == q? {p == q}') # False
print(f' ¿p == r? {p == r}') # True

# p y r apuntan al mismo objeto
# p y q apuntan a objetos distintos, aunque el contenido sea el mismo
# para comparar si contienen los mismos datos usamos el método __eq__ de la clase punto2D
