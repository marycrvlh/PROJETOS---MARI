opcao = ''

while opcao != '7':
    #tela de entrada
    print('='*40)
    print(f'{'CALCULADORA DE CONVERSÃO':^40}')
    print('='*40)
    print('| 1 - METROS -> KM                     |')
    print('| 2 - KM -> METROS                     |')
    print('| 3 - CM -> METROS                     |')
    print('| 4 - METROS -> CM                     |')
    print('| 5 - LITROS -> ML                     |')
    print('| 6 - ML -> LITROS                     |')
    print('| 7 - SAIR                             |')
    print('='*40)
    #escolha de opção e calculo de conversão    
    opcao = input('escolha uma opção: ')
    if opcao == '1': #conversão: metros para km 
        metros=int(input('digite o valor em metros: '))
        km_resultado=metros/1000
        print(f'resultado: {metros}m = {km_resultado:.2f} km')
    elif opcao == '2': #conversão: km para metros
       km=int(input('digite o valor em quilômetros: '))
       metros_resultado=km*1000
       print(f'resultado: {km}km = {metros_resultado:.2f} m')
    elif opcao == '3': #conversão: cm para metros
        cm=int(input('digite o valor em centímetros: '))
        metros_resultadodois=cm/100
        print(f'resultado: {cm}cm = {metros_resultadodois:.2f} m')
    elif opcao == '4': #conversão: metros para cm
        metros=int(input('digite o valor em metros: '))
        cm_resultado=metros*100
        print(f'resultado: {metros}m = {cm_resultado:.2f} cm')
    elif opcao == '5': #conversão: litros para ml
        litro=int(input('digite o valor em litros: '))
        ml_resultado=litro*1000
        print(f'resultado: {litro}L = {ml_resultado:.2f} ml')
    elif opcao == '6': #conversão: ml para litros
        ml=int(input('digite o valor em litros: '))
        litro_resultado=ml/1000
        print(f'resultado: {ml}ml = {litro_resultado}L')
    elif opcao == '7': #saí do menu
        print('saindo do programa...')
    else: #sinaliza uma mensagem de erro
        print('opção invalida. escolha uma opção dentro do menu.')
