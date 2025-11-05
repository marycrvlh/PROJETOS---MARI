import os
#criando o comando de limnpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
#criando um comando para exibir o menu
def exibir_menu():
    print('+='*20)
    print('        bem-vindo ao seu banco!    ')
    print('+='*20)
    print('\n escolha uma opção: ')
    print(' 1 - consultar saldo')
    print(' 2 - saque')
    print(' 3 - sair')
        
#crinado comando para consultar o saldo 
def consultar_saldo(saldo):
    print(f'seu saldo atual é: R${saldo:.2f}')
    
#criando o comando para continuar o programa
def pausa():
    input('\n pressione ENTER para continuar...')
    
#criando o comando para realizar o saque 
def realizar_saque(saldo):
    try: #tratamento de erro
        valor_saque = float(input('digite o valor do saque: '))
        if valor_saque <= 0: #se o saldo for negativo
            print('error: o valor do saque deve ser positivo.')
        elif valor_saque > saldo: #se o saque for maior que a quantidade de saldo
            print('error: saldo insuficiente para realizar o saque')
        else:
            saldo -= valor_saque #se o o saldo for maior que o valor do saque, ou seja, se tudo estiver conforme planejado
            print(f'saque realizadp com sucesso! \n seu saldo atual é de: R${saldo:.2f}')
    except ValueError:
        print('error: digite uma opção válida')
    return saldo
#fazendo o menu e suas opções
def main():
    saldo = 1000.00
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input('digite o número da opção desejada: ')
        
        if opcao == '1':
            consultar_saldo(saldo)
            pausa()
        elif opcao == '2':
            saldo = realizar_saque(saldo)
            pausa()
        elif opcao == '3':
            print('saindo do programa. até mais...')
            break
        else:
            print('opçaõ inválida. por favor, digite uma opção válida.')
            pausa()
            
    print("\n" + "=" * 30)
    print("      PROGRAMA ENCERRADO       ")
    print("=" * 30)
if __name__ == "__main__":  #chamnado o menu novamente
     main()
