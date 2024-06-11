lista_frutas = []
lista_talheres = []


lista = ['faca', 'morango', 'concha', 'laranja', 'colher de chá', 'uva', 'kiwi', 'banana', 'garfo', 'pera', 'colher']


for item in lista:
    if item in ['morango', 'laranja', 'uva', 'kiwi', 'banana', 'pera']:
        lista_frutas.append(item)  
    elif item in ['faca', 'concha', 'colher de chá', 'garfo', 'colher']:
        lista_talheres.append(item) 

print("Frutas:")
for fruta in lista_frutas:
    print(fruta)

print("\nTalheres:")
for talher in lista_talheres:
    print(talher)