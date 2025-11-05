import os
from datetime import datetime
import time

list_produtos = []
#criando a definição de limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#definição para retornar ao menu
def pausa():
    input('\n pressione ENTER para continuar...')

#definição para exibir o mennu
def exibir_menu():
    print('\n' + '='*60)
    print(' '*20 + 'MENU PRINCIPAL')
    print('='*60)
    print(f'{' 1 - adicionar produtos':<10}')
    print(f'{' 2 - exibir produtos':<10}')
    print(f'{' 3 - gerar cupom fiscal':<10}')
    print(f'{' 4 - sair':<10}')
    print('='*60)

#definição para adicionar um produto
def adicionar_produto():
    #pedindo os dados para o úsuario
     nome = input('digite o nome do produto (ou "sair" para finalizar): ')
     preco = float(input('digite o preço do produto: R$ '))
     quantidade = int(input('digite a quantidade de produtos que você deseja: '))
     dic_produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}  #organizando os dados em formato de dicionário
     list_produtos.append(dic_produto) #adicionando os dados à lista
     print(f'o {nome} foi adicionado com sucesso!')

#definição para exibir os dados na tela
def exibir_produtos():
    if not list_produtos:
        print('nenhum produto foi cadastrado.')
    else:
        print('\n' + '='*60)
        print(' '*20 + 'LISTA DE PRODUTOS')
        for i, p in enumerate(list_produtos, 1):
            print(f' {i}. {p['nome']} - R$ {p['preco']:.2f}')  #mostrando os dados e enumerando eles a partir do número um
    
#definição para gerar o cupom fiscal    
def gerar_cupom():
    if not list_produtos:
        print('nenhum produto foi cadastrado.')
        return
    else:
      data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    #layout do cupom fiscal
    print('\n' + '='*60)
    print(' '* 20 + 'CUPOM FISCAL SIMPLES')
    print('='*60)
    print(f'Data e Hora: {data_hora}')
    print('-'*60)
    print(f'{'Produto':<20}{'Qtd':<10}{'Preço unitário':<15}{'Total':<10}')
    print('-'*60)

    #listando produtos e calculando total da compra
    total_geral = 0
    for p in list_produtos:
        subtotal = p['preco']*p['quantidade']
        total_geral += subtotal
        print(f'{p['nome']:<20}{p['quantidade']:<10}{p['preco']:<15.2f}{subtotal:<10.2f}')
    
    print('-'*60)
    print(f'{'TOTAL GERAL':<30}{total_geral:>8.2f}')
    print('-'*60)
    print(' '*15 + 'obrigado pela preferência!')
    print('-'*60)  
    
#montando o menu
def main():
    while True:
      limpar_tela()
      exibir_menu()
      opcao = int(input('escolha uma opção: '))
    
      if opcao == 1:
        adicionar_produto()
        pausa()
      elif opcao == 2:
        exibir_produtos()
        pausa()
      elif opcao == 3:
         gerar_cupom()
         pausa()
      elif opcao == 4:
         print('\n saindo do programa.', end='')
         for i in range(5):
                print('.', end='', flush=True)
                time.sleep(0.5)
         print('\n programa encerrado com sucesso!')
         break
      else:
         print('opção invalida. digite uma opção válida.')
         pausa()
         
    print("\n" + "=" * 30)
    print("      PROGRAMA ENCERRADO       ")
    print("=" * 30)
    
if __name__ == '__main__':
    main()
