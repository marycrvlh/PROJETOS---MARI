#+======= criando uma lista vazia e adicionando itens ========+
#append: adiciona um dado novo na lista
lista_compras = []   #lista vazia

produto = input('digite o nome do produto: ') #solicita ao usuario um novo dado

lista_compras.append(produto) #adiciona o novo dado à lista vazia
print(lista_compras) #mostra a lista, agora com uma nova informação dada pelo usuario

#sofisticando e deixando o codigo mais bonito
print('\n lista de compras: ')
for item in lista_compras:
    print(f'- {item}')
    
#adicionando mais de um produto na lista
lista_compras = []
while True:
    produto = input('digite o nome do produto (ou "sair" para encerrar): ')
    #verificando se o usuario quer sair
    if produto.lower() == 'sair':
        print('encerrando o programa...')
        break
    #adicionando um produto na lista
    lista_compras.append(produto)
    #mostrando a lista atualizada
    print('\n lista de compras: ')
    for item in lista_compras:
        print(f'- {item}')