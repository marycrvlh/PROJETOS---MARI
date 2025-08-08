#solicita as informações do usuario
nome=input('digite seu nome: ')
idade=int(input('digite sua idade: '))

#compara a idade para a decisão
if idade<=13:
    print(f'olá {nome}, de acordo com a sua idade você é uma criança')
elif idade<18:
    print(f'olá {nome}, de acordo com a sua idade você é um adolescente')
else:
    print(f'olá {nome}, de acordo com a sua idade você é um adulto')