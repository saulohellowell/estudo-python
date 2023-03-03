
Frase = input('Digite uma frase: ')

i = 0
apareceu_mais_x = 0
letra_apareceu_mais_x =''

while i < len(Frase):
    letra_atual = Frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    qnt_x_letra_apareceu = Frase.count(letra_atual)
    
    
    if apareceu_mais_x < qnt_x_letra_apareceu:
        apareceu_mais_x = qnt_x_letra_apareceu
        letra_apareceu_mais_x = letra_atual
    
    i += 1
print(f'a letra que mais apareceu foi {letra_apareceu_mais_x}, '
 f'ela apareceu {apareceu_mais_x}'
)
print(len(Frase))    
    
    
    