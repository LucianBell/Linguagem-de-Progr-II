"""
Implemente a classe Empregado como uma subclasse de  Pessoa.  Considere que  cada  instância  da classe
Empregado  tem,  além  dos  atributos  que caracterizam  a  classe  Pessoa,  os  atributos
salarioBase (vencimento  base)  e  mesesTrabalhados (quantidade de meses trabalhados no ano corrente).


Empregado  deve conter um construtor que invoca o construtor da classe Pessoa, os  métodos
setters/getters  e  um  método calcularSalario que retorna o salário base múltiplicado pelos meses
trabalhados.

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


class Empregado(Pessoa):
    def __init__(self, nome, endereco, salarioBase, mesesTrabalhados):
        super().__init__(nome, endereco)
        self.salarioBase = salarioBase
        self.mesesTrabalhados = mesesTrabalhados

    def get_salarioBase(self):
        return self.salarioBase

    def set_salarioBase(self, salarioBase):
        self.salarioBase = salarioBase

    def get_mesesTrabalhados(self):
        return self.mesesTrabalhados

    def set_mesesTrabalhados(self, mesesTrabalhados):
        self.mesesTrabalhados = mesesTrabalhados

    def calcularSalario(self):
        return self.salarioBase * self.mesesTrabalhados


# Programa de teste
empregado1 = Empregado("Empregado A", "Rua Y", 3000, 6)

print("Nome do Empregado:", empregado1.get_nome())
print("Endereço do Empregado:", empregado1.get_endereco())
print("Salário Base do Empregado:", empregado1.get_salarioBase())
print("Meses Trabalhados do Empregado:", empregado1.get_mesesTrabalhados())
print("Salário do Empregado:", empregado1.calcularSalario())