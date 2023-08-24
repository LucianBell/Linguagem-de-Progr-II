"""
Escreva um modelo Empregado que represente um empregado de uma empresa qualquer. Considere que os atributos
nome, departamento, horasTrabalhadasNoMês e salárioPorHora devam ser representados, e que ao menos as
operações mostraDados e calculaSalárioMensal sejam implementadas.
"""


class Empregado:
    def __init__(self, nome, departamento, horasTrabalhadasNoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasNoMes = horasTrabalhadasNoMes
        self.salarioPorHora = salarioPorHora

    def calcula_salario_mensal(self):
        return self.salarioPorHora * self.horasTrabalhadasNoMes

    def mostra_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Departamento: {self.departamento}")
        print(f"Horas Trabalhadas no Mês: {self.horasTrabalhadasNoMes}")
        print(f"Salário Por Hora: {self.salarioPorHora}")
        print(f"Salário Mensal: {self.calcula_salario_mensal()}")


empregadoTeste = Empregado("teste", "testinha", 12, 2.0)
print(empregadoTeste.nome)
print(empregadoTeste.calcula_salario_mensal())
empregadoTeste.mostra_dados()
