"""
Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura.
Crie os métodos públicos necessários para sets e gets e também um métodos para imprimir os
dados de uma pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        print(f"Nome: {self.__nome}")

    def get_idade(self):
        print(f"Idade: {self.__idade}")

    def get_altura(self):
        print(f"Altura: {self.__altura}")

    def set_nome(self, nome_novo):
        self.__nome = nome_novo
        print(f"Novo nome: {self.__nome}")

    def set_idade(self, idade_novo):
        self.__idade = idade_novo
        print(f"Nova idade: {self.__idade}")

    def set_altura(self, altura_novo):
        self.__altura = altura_novo
        print(f"Nova altura: {self.__altura}")

    def mostrar_dados(self):
        print("DADOS")
        print(f"Nome: {self.__nome}\nIdade: {self.__idade}\nAltura: {self.__altura}")


pessoa_teste = Pessoa("Axl", 21, 178)
pessoa_teste.mostrar_dados()
pessoa_teste.set_altura(182)
pessoa_teste.set_idade(19)
pessoa_teste.set_nome("Slash")
pessoa_teste.mostrar_dados()