
numero = input('digite um numero inteiro: ')
"""

if numero.isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print('esse numero e par!!!')
    else:
        print('esse numero e impar!!!')

else:
    print('esse nao e um numero inteiro')
"""

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("esse e um numero par")
    else:
        print('esse e um numero impar')

except:
    print('esse nao e um numero inteiro')
