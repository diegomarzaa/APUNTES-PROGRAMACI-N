número = int(input("Número: "))

es_primo = True
for divisor in range(2, número):                                       # Si no hay ningun divisor entre 2 y n - 1, el número es primo
    if número % divisor == 0:                                          # Empiezas siendo optimista y asumiendo que es primo, y luego cuando encuentres un divisor lo cambias a falso
        es_primo = False
        break # Termina ejecución del bucle for


# Reescribe el programa anterior, pero sin usar break 
es_primo = True
divisor = 2
while divisor < número and es_primo:
    if número % divisor == 0:
        es_primo = False
    divisor += 1