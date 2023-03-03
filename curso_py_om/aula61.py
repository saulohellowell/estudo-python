contador = 0

while contador <100:
    contador +=1
    if contador == 6:
        print('pulei')
        continue

    if contador >10 and contador < 39:
        continue

    print(contador)

    if contador == 40:
        break

print('acabou')    