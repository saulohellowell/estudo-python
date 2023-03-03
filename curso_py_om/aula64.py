

# objetivo colocar * entre as letras do nome

nome = input('digite um nome: ')
tamanho_do_nome = len(nome)
contador_nome = 0
objetivo = ''

while contador_nome < tamanho_do_nome:
    letra = nome[contador_nome]
    objetivo += f'*{letra}'
    contador_nome += 1

print(objetivo)   