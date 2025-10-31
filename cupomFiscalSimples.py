from datetime import datetime
#script para cupom fiscal simples

#dicionario vazio
dic_produtos = {}

#inserindo os dados
while True:
    produto = input('digite o nome do produto (ou "sair" para finalizar): ')
    if produto.lower() == 'sair':
        break
    preco = float(input('digite o preço do produto: R$ '))
    quantidade = int(input('digite a quantidade de produtos que você deseja: '))
    dic_produtos[produto] = {'preco' : preco , 'quantidade' : quantidade}
#crinado uma variavel para data 
data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

#layout do cupom fiscal
print('\n' + '='*60)
print(' '* 20 + 'CUPOM FISCAL SIMPLES')
print('='*60)
print(f'Data e Hora: {data_hora}')
print('-'*60)
print(f'{'Produto':<20}{'Qtd':<10}{'Preço unitário':<15}{'Total':<10}')
print('-'*60)

#listando produtos e calculando total da compra
total_geral = 0
for produto, dados in dic_produtos.items():
    subtotal = dados['preco']*dados['quantidade']
    total_geral += subtotal
    print(f'{produto:<20}{dados['quantidade']:<10}{dados['preco']:<15.2f}{subtotal:<10.2f}')
    
print('-'*60)
print(f'{'TOTAL GERAL':<30}{total_geral:>8.2f}')
print('-'*60)
print(' '*15 + 'obrigado pela preferência!')
print('-'*60)