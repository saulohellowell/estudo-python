
texto = 'montreal'
i = 0 
nova_string = ''

for letra in texto:
    nova_string += f'*{letra}'
    print(letra, i)
    print(nova_string)

    i += 1
print(f'{nova_string}*')    