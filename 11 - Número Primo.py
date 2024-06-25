numero = 23  # número que queremos verificar se é primo

if numero > 1:  # primos são maiores que 1
    # verificando se há algum divisor além de 1 e do próprio número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f'{numero} não é um número primo.')
            break
    else:
        print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')
