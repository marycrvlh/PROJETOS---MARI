#+======= remover um item da lista ========+
lista_compras = []
#pedindo ao usuario para digitar o produto
while True:
    produto = input('digite o nome do produto, "remover nome_do_produto" para remover um produto ou "sair" para encerrar: ') #iserção do produto
    
    if produto.lower() == 'sair':
        print('encerrando produto')
        break
    
    #verifica se o usuario quer remover um produto
    if produto[:8].lower() == 'remover ':
    #fazendo um comparativo, se o produto que o usuario digitar tiver 8 letras e for igual a palavra remover ele vai entender que necessita remover o produto
        item_remover = produto[8:].strip() #strip: tira os espaços que o usuario digitar
        if item_remover in lista_compras:
            lista_compras.remove(item_remover) #remove: é para remover o item que o usuario escreveu
            print(f'{item_remover} foi removido da lista')
        else:
            print(f'o produto "{item_remover}" não está na lista')
    else:
        lista_compras.append(produto)
        print(f'{produto} foi adicionado à lista')
    
    print('\n lista de compras: ')
    if lista_compras:
        for item in lista_compras:
            print(f'- {item}')
    else:
        print('a lista está vazia')