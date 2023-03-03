

lista_compras = []
f = open("listacompras.txt", "w")
f.write("sua lista de compras:\n")
f.close()


while True:

    acao = input('digiti [i]nserir, [a]pagar ou [l]istar: ')
   
    if acao == 'i':
        item_inserir = input('o que voce deseja adicionar a sua lista: ')
        lista_compras.append(item_inserir)

    elif acao == 'a':
        item_apagar = input('qual item voce dejesa apagar:')
        if item_apagar in lista_compras:
            lista_compras.remove(item_apagar)
        else:
            print('este item nao esta na sua lista de compras!')
        

        
    elif acao == 'l':
        for index, item in enumerate(lista_compras):
            print(index, item)

    else:
        print('voce precisa digitar uma das opcoes!')     
        continue

    sair = input('deseja continuar S/N? ')
    if sair == 'N':
        
        produto_str = " \n".join(lista_compras)
        
        f = open("listacompras.txt", "a")
        f.write(produto_str)
        f.close()
        f = open("listacompras.txt", "r")
        print(f.read())

        break
    else:
        continue
