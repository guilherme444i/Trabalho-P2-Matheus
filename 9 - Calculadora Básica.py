
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


opcao = input("Digite o número da operação desejada (1/2/3/4): ")


opcao = int(opcao)


if opcao < 1 or opcao > 4:
    print("Opção inválida.")
else:
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

   
    if opcao == 1:
        resultado = num1 + num2
        operacao = "+"
    elif opcao == 2:
        resultado = num1 - num2
        operacao = "-"
    elif opcao == 3:
        resultado = num1 * num2
        operacao = "*"
    elif opcao == 4:
        
        if num2 == 0:
            print("Erro: divisão por zero.")
        else:
            resultado = num1 / num2
            operacao = "/"
    
    # Exibe o resultado da operação
    print(f"O resultado de {num1} {operacao} {num2} é {resultado}")
