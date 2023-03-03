nome = input('digite seu nome: ')
idade = input('digite a sua idade: ')

len_nome = len(nome)
len_idade = len(idade)



if len_nome and len_idade >= 1:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espacos')

    else:
        print('Seu nome nao tem espaco')    

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é: {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[(len_nome - 1)]}')


else:
    print('desculpe, voce deixou campos vazios')


 
