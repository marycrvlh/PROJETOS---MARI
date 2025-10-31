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
    
