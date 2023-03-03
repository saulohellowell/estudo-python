

hora = input('digiti uma hora: ')

try:
    hora_int = int(hora)
    if hora_int <= 11:
        print('bom dia 0-11')
    elif hora_int >=12 and hora_int <= 17:
        print('boa tarde 12-17')
    elif hora_int >= 18 and hora_int <= 23:
        print('boa noite 18-23')
    else:
        print('voce digitou um numero maior que 24')

except:
    print('voce digitou algo diferente de numeros')
    