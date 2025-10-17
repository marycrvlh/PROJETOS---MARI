dic_produto = {'arroz': 20.00, 'feijão': 7.5, 'macarrão': 5.0, 'carne': 25.0}

#listar elemento do dicionario
print(dic_produto['carne'])

#adicionar um elemento ao dicionario
dic_produto['ovos grandes'] = 16.0
print(dic_produto)

#editar um elemento e adicionar um aumento de 30%
dic_produto['carne'] = dic_produto['carne'] * 1.3
print(dic_produto)

#quantidade de elementos no dicionario
print(len(dic_produto))

#remover um elemento do dicionario
dic_produto.pop('macarrão')
print(dic_produto)
