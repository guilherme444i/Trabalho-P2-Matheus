# Inicializa uma variável para acumular a soma dos números
soma = 0

# Loop para pedir os 10 números
for i in range(1, 11):  # i varia de 1 a 10 (inclusive)
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

# Exibe a soma dos 10 números
print(f"A soma dos 10 números é: {soma}")