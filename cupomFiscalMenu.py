import os
from datetime import datetime

#criando a definição de limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print('\n' + '='*60)
    print(' '*20 + 'MENU PRINCIPAL')
    print('='*60)
    print(f'{' 1 - adicionar produtos':<10}')
    print(f'{' 3 - exibir produtos':<10}')
    print(f'{' 3 - gerar cupom fiscal':<10}')
    print(f'{' 4 - sair':<10}')
    print('='*60)
    print('escolha uma opção: ')

  
def adicionar_produto():
     produto = input('digite o nome do produto (ou "sair" para finalizar): ')
     preco = float(input('digite o preço do produto: R$ '))
     quantidade = int(input('digite a quantidade de produtos que você deseja: '))
     print(f'o {produto} foi adicionado com sucesso!')

def exibir_produtos():
    
def main():
    produtos = {}
    while True:
      limpar_tela()
      exibir_menu()
      opcao = int(input('escolha uma opção: '))
    
      if opcao == '1':
        adicionar_produto()
        pausa()
      elif opcao == '2':
     
      elif opcao == '3':
         
      elif opcao == '4':
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
