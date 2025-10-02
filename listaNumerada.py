#+======= númera a lista ========+
lista_compras = []
while True: #enquanto a condição for verdadeira
    produto = input('digite o nome do produto (ou "sair" para encerrar): ')
    #verificando se o usuario quer sair
    if produto.lower() == 'sair': #lower: converte todos os caracteres para minusculo
        print('encerrando o programa...')
        break #quebra a continuidade da condição/interrompe o programa 
    #adicionando um produto na lista
    lista_compras.append(produto)
    #mostrando a lista atualizada
    print('\n lista de compras: ')
    for i,item in enumerate(lista_compras, start=1):
                #enumerate tem a função de enumerar os itens da lista
                #start é para indicar qual nùmero vai começar a contagem
        print(f'{i} - {item}')