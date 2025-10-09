import os

lista_compras = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #limpando a tela
    produto = input('digite o nome de um produto (ou "sair" para encerrar): ')
    
    #verificando se o usuario quer sair
    if produto.lower() == 'sair':
        print('saindo do programa. até mais!')
        break
    
    #adicionando produtos à lista
    lista_compras.append(produto)
    
    #mostrando a lista enumerada e atualizada
    print('\n lista de compras: ')
    for i, item in enumerate(lista_compras, start=1 ):
        print(f"{i} - {item}")
        
    input('\n pressione Enter para continuar...') #pausa antes de limpar a tela de novo