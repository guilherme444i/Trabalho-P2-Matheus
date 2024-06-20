entrada = input("Digite os números separados por espaço: ")

lista_numeros = list(map(float, entrada.split()))

if not lista_numeros:
    print("Não foi fornecido nenhum número.")
else:
    
    maior_numero = menor_numero = lista_numeros[0]
    
    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
    
    # Exibe os resultados
    print(f"O maior número é: {maior_numero}")
    print(f"O menor número é: {menor_numero}")
