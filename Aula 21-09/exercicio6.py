"""

"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pessoa(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")


class Pobre(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def trabalha(self):
        print("Trabalhando :(")


class Rico(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro

    def faz_compras(self):
        print("Fazendo comprinhas...")
        self.dinheiro -= 10.0


class Miseravel(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)

    def mendiga(self):
        print("Mendigando :(")