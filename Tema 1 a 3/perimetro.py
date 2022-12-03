from math import pi

# Pedir valor del radio
radio = int(input("Dame el radio: "))

# Realizar cálculos
longitud = 2 * pi * radio
area = pi * radio ** 2
volumen = 4 / 3 * pi * radio ** 3


# Mostrar resultados
print('longitud =', longitud)
print('area =', area)
print('volumen =', volumen)
