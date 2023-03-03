

nome = input('escreva seu nome: ')
nome_len = len(nome)

try:
    nome_int = int(nome)
    print('voce nao digitou numeros!')
   
except:
    if nome_len <= 4:
        print('seu nome e curto')
    elif nome_len == 5 or nome_len == 6:
        print('seu nome e normal')
    else:
        print('seu nome e muito grande')
    print('voce nao digitou um numero')
