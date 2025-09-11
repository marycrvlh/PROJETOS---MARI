#tela de entrada
print('='*40)
print(f'{'SISTEMA DE CONTROLE DE HORAS':^40}')
print('='*40)
#entrada de dados
nome=input('digite o nome do funcionario: ').capitalize()
codigo=int(input('digite o codigo de registro desse funcionario: '))
numDeHorasTrabalhadas=int(input('digite o número de horas trabalhadas desse funcionario: '))
valorDeHrsTrabalhadas=int(input('digite o valor que recebe por hora trabalhada (R$): '))
#cálculo do sálario
salarioTotal=valorDeHrsTrabalhadas*numDeHorasTrabalhadas
#tela de saída
print('\n' + '='*40)
print(f'{'nome':<20}: {nome}')
print(f'{'identificação':<20}: {codigo}')
print(f'{'horas trabalhadas':<20}: {numDeHorasTrabalhadas}')
print(f'{'salario por hora':<20}: {valorDeHrsTrabalhadas:.2f}')
print(f'{'salario do dia':<20}: {salarioTotal:.2f}')
print('='*40)