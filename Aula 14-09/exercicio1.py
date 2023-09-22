"""
Implemente uma classe Pessoa, com os atributos nome, endereco. A classe deve ter um construtor que receba como
parâmetro o nome e o endereço da pessoa, bem como os devidos métodos getters e setters.
"""


class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco
