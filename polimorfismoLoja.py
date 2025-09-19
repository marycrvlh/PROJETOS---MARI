#classe loja
#PRODUTOS DA LOJA: LIVRO, ELETRONICOS E ALIMENTOS

class Produtos:
    def __init__(self, preco, codigo):
        self.preco = preco  #atributos da classe mãe
        self.codigo = codigo
    def descricao(self):
        return f'o produto {self.codigo} custa R${self.preco}.'
    
#classe filha: livros
class Livros(Produtos):
    def __init__(self, preco, codigo, pagina):
        super().__init__(preco, codigo) #inicializa atributos da mãe
        self.pagina = pagina #atributo especifico da filha
    def descricao(self): #polimorfismo de sobreposição (override)
        return f'o livro {self.codigo} custa R${self.preco}, tem {self.pagina} páginas.'
    
#classe filha: eletrônico
class Eletronico(Produtos):
    def __init__(self, preco, codigo, marca):
        super().__init__(preco, codigo) 
        self.marca = marca
    def descricao(self):
        return f'o eletrônico {self.codigo} custa R${self.preco} é da marca {self.marca}.'
    
#classe filha: alimento
class Alimento(Produtos):
    def __init__(self, preco, codigo, tipo):
        super().__init__(preco, codigo)
        self.tipo = tipo
    def descricao(self):
        return f'o alimento {self.codigo} custa R${self.preco}, é do tipo {self.tipo}.'

#+======= criando objetos ========+
livro1 = Livros('R$45,99', 'cod.2525', '200')
eletronico1 = Eletronico('R$79,99', 'cod.2009', 'kaidi')
alimento1 = Alimento('R$2,99', 'cod.12', 'fruta')

#+======= testando o polimorfismo ========+
print(livro1.descricao()) #isso chama o método da filha
print(eletronico1.descricao())
print(alimento1.descricao())