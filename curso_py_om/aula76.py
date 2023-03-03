
import random

palavras = ['montreal', 'canada', 'brasil', 'portugal', 'argentina']

palavra_secreta = random.choice(palavras)
letra_acertada = ''
letras_erradas = '' 
numero_tentativas =  0

while True:
        if numero_tentativas > 10:
                print('as letras que voce voce digitou foram', letras_erradas)
                print('voce perdeu')
                break

        letra_digitada = input('digite uma letra: ')
        numero_tentativas += 1

        if len(letra_digitada) > 1:
                print('voce digitou mais de uma letra: ')
                continue
        

        if letra_digitada in letra_acertada or letra_digitada in letras_erradas:
                print('voce ja digitou', letra_digitada)
                continue
        

        if letra_digitada in palavra_secreta:
                letra_acertada += letra_digitada
        else:
                letras_erradas += letra_digitada        

        palavra_acertada = ''
        for letra_secreta in palavra_secreta:
                if letra_secreta in letra_acertada:
                        palavra_acertada += letra_secreta
                else:
                        palavra_acertada += '*'   

        if palavra_acertada == palavra_secreta:
                print('voce acertou a palavra secreta e', palavra_secreta)
                print('voce tentou', numero_tentativas, 'vezes')
               
                if len(letras_erradas) > 0:
                        print('voce errou as letras', letras_erradas)
                else:
                        print('voce nao errou nenhuma letra')
                
                novo_jogo = input('voce gostaria de jogar de novo: S ou N ')
                if novo_jogo == 'S':
                        palavra_secreta = random.choice(palavras)
                        letra_acertada = ''
                        letras_erradas = '' 
                        numero_tentativas =  0  
                        
                else:        
                        break

        else:
                print(palavra_acertada)   
 

        

