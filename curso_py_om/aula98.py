

cpf = input('digite seu cpf (xxx.xxx.xxx-xx): ')
cpf_lista = list(cpf)

del cpf_lista[3]
del cpf_lista[6]
del cpf_lista[9]
cpf_calculo = cpf_lista[:9]


multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
#                   7  1  5  8  0  2  3  9  1
cpf_int = []
for item in cpf_calculo:
    cpf_int.append(int(item))
          
lista_somadas = [x*y for x,y in zip(cpf_int, multiplicadores)]

digito_1 = (sum(lista_somadas)*10)%11


#calculo do segundo digito

cpf_int_2 = cpf_int
cpf_int_2.append(digito_1)
mutiplicadores_2 = [11,10,9,8,7,6,5,4,3,2]

item_somados_2 = [x*y for x,y in zip(cpf_int_2, mutiplicadores_2)]
digito_2 = (sum(item_somados_2)*10)%11


if digito_1 == int(cpf_lista[-2]) and digito_2 == int(cpf_lista[-1]):
    print('cpf valido')

else:
    print('cpf invalido')

