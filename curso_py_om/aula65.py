
# calculadora
while True:
    num_1 = input('digite um numero: ')
    num_2 = input('digite outro numero: ')  
    operador = input('digite um operador (+ - * /): ')
    num_valido = None
    float_num_1 = 0
    float_num_2 = 0

    try:
        float_num_1 = float(num_1)
        float_num_2 = float(num_2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None:
        print('voce digitou algo diferente de numeros')
        continue 

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('voce digitou um operador nao valido')
        continue

    if len(operador) > 1 :
        print('voce digitou mais de um operador')
        continue

    if operador == '+' :
        print(f'{float_num_1} + {float_num_2} = {float_num_1 + float_num_2}')
    elif operador == '-' :
        print(f'{float_num_1} - {float_num_2} = {float_num_1 - float_num_2}')
    elif operador == '*':
        print(f'{float_num_1} * {float_num_2} = {float_num_1 * float_num_2}')    
    elif operador == '/':
        print(f'{float_num_1} / {float_num_2} = {float_num_1 / float_num_2}')
    else:
        print('erro desconhecido kkkkkk')

    sair = input('Deseja Sair: ')
    if sair == 'sim':
        print('saiu')
        break
    
