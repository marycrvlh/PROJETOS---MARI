#exibindo uma informação na tela
print('olá aventureiro!')

#armazenamento de dados em uma váriavel
nome = input('diga-me qual o seu nome? ')
idade = int(input('qual sua idade?' ))
print(f'seja bem-vindo {nome}... humm, então você tem {idade} anos? você parece ter idade suficiente para responder a seguinte pergunta...')

#loop true while
while True:
    dedos = int(input('quantos dedos um ser humano tem em uma mão? '))
    if dedos == 5:
        print('exatamente! você é realmente uma pessoa muito esperta')
        break
    else:
        print('ERRADO! te darei outra chance...')

#+===== inventario: menu e lista ======+
opcao = ''
while opcao != '4':
    print('='*30)
    print('|         M E N U            |')
    print('='*30)
    print('| 1 - suprimentos             |')
    print('| 2 - armas                   |')
    print('| 3 - armadura                |')
    print('| 4 - sair                    |')
    print('='*30)
    
    opcao = input('para começar essa jornada você irá precisar de alguns equipamentos. o que você gostaria de dar uma olhada? ')
    
    if opcao == '1':
     print('='*30)
     print('|        suprimentos         |')
     print('='*30)
     print('| - pacotes de saúde         |')
     print('| - munição                  |')
     print('| - materiais de fabricação  |')
     print('='*30)
     break
    elif opcao == '2':
     print('='*30)
     print('|            armas           |')
     print('='*30)
     print('| - foice                    |')
     print('| - machado                  |')
     print('| - arma magnum              |')
     print('='*30)
     break
    elif opcao == '3':
     print('='*30)
     print('|                                                  armadura                                             |')
     print('='*30)
     print('| - armaduras leves (como tecido ou couro, para mobilidade e bónus mágicos)                             |')
     print('| - armaduras pesadas (como placas de metal ou armaduras energéticas, para defesa física e resistência) |')
     print('='*30)
     break
    elif opcao == '4':
        print(f'até mais, jovem aventureiro {nome}!')
    else:
        print('ops... parece que não temos essa opção, tente outra.')
        
resposta = input('deseja comprar algo? ')
if resposta == 'sim'.lower():
 print('bom, o que deseja?')
elif resposta == 'nao'.lower():
 print('então, vamos dar uma olhada nas coisas que você tem dentro desta bolsa')

