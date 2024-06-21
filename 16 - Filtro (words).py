# Lista de palavras
palavras = ["python", "java", "c++", "javascript", "php", "ruby", "go"]

# Solicita ao usuário uma letra
letra_desejada = input("Digite uma letra para encontrar palavras que começam com ela: ")


print(f"Palavras que começam com '{letra_desejada}':")
for palavra in palavras:
    if palavra.lower().startswith(letra_desejada.lower()):
        print(palavra)