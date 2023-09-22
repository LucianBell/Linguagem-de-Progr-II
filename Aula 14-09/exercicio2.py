"""
Criar uma classe Fornecedor derivada de Pessoa. Considere  que cada  instância  de Fornecedor  tem
, além dos atributos que caracterizam  a classe Pessoa, os atributos credimaximo (correspondente  ao
crédito  máximo  atribuído  pelo  fornecedor  a  determinada pessoa)  e  valorEmDivida  (montante  da
  dívida  para com  o  fornecedor).

Fornecedor deve conter um construtor que invoca o construtor da classe Pessoa e também os  usuais métodos
setters/getters. Além disso, deve existir um método obterSaldo que devolve a diferença entre os valores
dos atributos credimaximo e valorEmDivida

Escreva um programa de teste adequado para esta classe.
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


class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, credimaximo, valorEmDivida):
        super().__init__(nome, endereco)
        self.credimaximo = credimaximo
        self.valorEmDivida = valorEmDivida

    def get_credimaximo(self):
        return self.credimaximo

    def set_credimaximo(self, credimaximo):
        self.credimaximo = credimaximo

    def get_valorEmDivida(self):
        return self.valorEmDivida

    def set_valorEmDivida(self, valorEmDivida):
        self.valorEmDivida = valorEmDivida

    def obterSaldo(self):
        return self.credimaximo - self.valorEmDivida


# Programa de teste
fornecedor1 = Fornecedor("Fornecedor A", "Rua X", 10000, 5000)

print("Nome do Fornecedor:", fornecedor1.get_nome())
print("Endereço do Fornecedor:", fornecedor1.get_endereco())
print("Crédito Máximo do Fornecedor:", fornecedor1.get_credimaximo())
print("Valor em Dívida do Fornecedor:", fornecedor1.get_valorEmDivida())
print("Saldo do Fornecedor:", fornecedor1.obterSaldo())