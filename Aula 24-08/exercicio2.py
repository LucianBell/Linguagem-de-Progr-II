"""
Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura.
Crie os métodos públicos  necessários para sets e gets e também um métodos para imprimir os
dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura