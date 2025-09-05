#Escreva um programa que leia o nome e codigo de um funcionário, seu número de horas trabalhadas,
# o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

#solicita as informações do funcionario
nome=input('digite o nome do funcionario: ')
codigo=int(input('digite o codigo de registro desse funcionario: '))
numDeHorasTrabalhadas=int(input('digite o número de horas trabalhadas desse funcionario: '))
valorDeHrsTrabalhadas=int(input('digite o valor que recebe por hora trabalhada: '))

#calculo do salario desse funcionario
salarioFuncionario = numDeHorasTrabalhadas*valorDeHrsTrabalhadas

#tabela de informações
print('-='*27)
print('|                      BEM-VINDO                     |')
print('-='*27)
print(f'| 1 - nome: {nome}                   ')
print(f'| 2 - código: {codigo}                 ')
print(f'| 3 - número de horas trabalhadas: {numDeHorasTrabalhadas}  ')
print(f'| 4 - valor que o funcionario recebe por horas: R${valorDeHrsTrabalhadas}  ')
print(f'| 5 - salario calculado: R${salarioFuncionario}      ')
print('-='*27)


#apresenta o resultado
print(f'o funcionario {nome} com o código {codigo}, possui o salário de R${salarioFuncionario} de acordo com suas horas de trabalho.')
