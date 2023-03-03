qtd_linha = input('quantidade de linhas: ')
qtd_colunas = input('quantidade de colunas: ')

int_linha = int(qtd_linha)
int_coluna = int(qtd_colunas)

linha = 1
while linha <= int_linha:
    coluna = 1
    while coluna <= int_coluna:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('acabou')
        