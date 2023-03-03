

primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

resposta1 = f'o numero {primeiro_valor} é maior que o numero {segundo_valor}'
resposta2 = f'o numero {primeiro_valor} é menor que o numero {segundo_valor}'
resposta3 = f'o numero {primeiro_valor} é igual ao numero {segundo_valor}'


if primeiro_valor > segundo_valor:
    print(resposta1)
elif primeiro_valor < segundo_valor:
    print(resposta2)
elif primeiro_valor == segundo_valor:
    print(resposta3)
else:
    print('voce precisa digitar um valor!')  
      
    
