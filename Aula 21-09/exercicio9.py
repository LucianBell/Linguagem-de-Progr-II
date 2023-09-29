class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def imprimeEndereco(self):
        print(f'Endereço: {self.endereco}')

    def imprimePreco(self):
        print(f'Preço: R$ {self.preco:.2f}')


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def acessoAdicional(self):
        return self.adicional

    def imprimeAdicional(self):
        print(f'Adicional: R$ {self.adicional:.2f}')


class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def acessoDesconto(self):
        return self.desconto

    def imprimeDesconto(self):
        print(f'Desconto: R$ {self.desconto:.2f}')
