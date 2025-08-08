#solicita os dados do aluno
nome=input('digite o nome do aluno: ')
nota1=float(input('digite a nota do aluno: '))
nota2=float(input('digite a nota do aluno: '))
nota3=float(input('digite a nota do aluno: '))
nota4=float(input('digite a nota do aluno: '))

#calcula a média das notas
mediaNota=(nota1+nota2+nota3+nota4)/4
print(f"a média do aluno {nome} é de {mediaNota}")

#faz a comparação
if mediaNota>=7:
    print('o aluno está aprovado')
elif mediaNota >=5 or <=7:
    print('o aluno está de recuperação')
else:
    print('o aluno está reprovado')