opcao = ''

while opcao != '4':
    print('='*30)
    print('|         M E N U            |')
    print('='*30)
    print('| 1 - dizer olá              |')
    print('| 2 - somar dois números     |')
    print('| 3 - subtrair dois números  |')
    print('| 4 - sair                   |')
    print('='*30)
    
    opcao = input('escolha uma opção: ')
    if opcao == '1':
        print('olá! seja bem-vindo')
    elif opcao == '2':
        num1=float(input('digite o primeiro número:'))
        num2=float(input('digite o segundo número: '))
        soma = num1+num2
        print(f'a soma de {num1} e {num2} é igual a {soma:.2}')
    elif opcao == '3':
        num1=float(input('digite o primeiro número: '))
        num2=float(input('digite o segundo número: '))
        subtrai = num1-num2
        print(f'a subtração de {num1} e {num2} é igual a {subtrai:.2}')
    elif opcao == '4':
        print('saindo do programa. até logo!')
    else:
        print('opção invalida. escolha uma opção do menu.')