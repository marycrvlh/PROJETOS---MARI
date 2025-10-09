import os

def Limpar_Tela():
    os.system('cls' if os.name == "nt" else 'clear')
    
lista_compras = []
opcao = 0

while opcao != 4:
    Limpar_Tela()
    
    print('===== LISTA DE COMPRAS =====')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - ver a lista')
    print('4 - sair')
    print('============================')
    
    #tratamento de erro
    try:
     opcao = int(input('digite uma opção do menu: '))
    except:
     continue
 
    #adicionar item
    if opcao == '1':
        produto = input('digite o nome do produto: ')
        lista_compras.append(produto)
        print('\n lista de compras: ')
        for item in lista_compras:
            print(f'- {item}')