"""
Crie um programa para representar funcionarios em um sistema de gestao de pessoas.

É necessario que nesta modelagem seja feito de uso de no minimo duas classes e com uma associacao entre estas.
Cada classe deverá ter no mínimo 2 atributos.
"""


class Gestor:
    def __init__(self, nome, xp):
        self.nome = nome
        self.xp = xp

    def gerenciar(self):
        print("gerenciando...")


class Funcionario:
    def __init__(self, nome, cargo, gestor):
        self.gestor = gestor
        self.cargo = cargo
        self.nome = nome

    def set_gestor(self, gestor):
        self.gestor = gestor


if __name__ == '__main__':
    gestor_joao = Gestor("João", 5)
    funcionario_maria = Funcionario("Maria", "Desenvolvedora", gestor_joao.nome)

    print("Gestor da maria ->", funcionario_maria.gestor)
