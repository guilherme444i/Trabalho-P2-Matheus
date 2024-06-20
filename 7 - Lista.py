# Inicializa uma lista vazia para armazenar os elementos
lista_elementos = []

# Loop para adicionar elementos até que o usuário digite "parar"
while True:
    elemento = input("Digite um elemento para adicionar à lista (ou digite 'parar' para encerrar): ")
    if elemento.lower() == 'parar':
        break
    lista_elementos.append(elemento)

# Exibe a lista completa
print("Lista completa:")
print(lista_elementos)
