#gerador de cpf
import random
from random import choices, sample
tamanho = 9
quais_numeros = range(0,10) 
lista_numeros = choices(quais_numeros, k=tamanho)


multiplicadores = [10,9,8,7,6,5,4,3,2]
soma_listas = [x*y for x,y in zip(lista_numeros, multiplicadores)]

digito_1 = (sum(soma_listas)*10)%11

if digito_1 >=10:
    digito_1 = 0
else:
    digito_1 = digito_1
   

#segundo digito

lista_numeros.append(digito_1)
multiplicadores.insert(0, 11)

soma_listas_2 = [x*y for x,y in zip(multiplicadores, lista_numeros)]
digito_2 = (sum(soma_listas_2)*10)%11

digito_2 = digito_2 if digito_2 <= 9 else 0
lista_numeros.append(digito_2)

list_numeros_str = []

for item in lista_numeros:
    list_numeros_str.append(str(item))


list_numeros_str.insert(3, '.')
list_numeros_str.insert(7, '.')
list_numeros_str.insert(11, '-')



cpf = ''.join(list_numeros_str)
print(cpf)