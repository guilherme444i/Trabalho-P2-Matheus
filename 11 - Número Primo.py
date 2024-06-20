import math

# Número a ser verificado
numero = 17

# Verificar se é menor ou igual a 1
if numero <= 1:
    eh_primo = False
else:
    eh_primo = True

    # Verificar se é divisível por algum número além de 1 e ele mesmo
    limite = int(math.sqrt(numero)) + 1
    for i in range(2, limite):
        if numero % i == 0:
            eh_primo = False
            break

# Resultado
if eh_primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
