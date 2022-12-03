es_primo = True
for divisor in range(2, número):
    if número % divisor == 0:
        es_primo = False
        break # Termina ejecución del bucle for