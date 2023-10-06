"""
Escreva um modelo Empregado que represente um empregado de uma empresa qualquer.
Considere que os atributos nome, departamento, horasTrabalhadasNoMês e salárioPorHora devam ser representados,
e que ao menos as operações mostraDados e calculaSalárioMensal sejam implementadas.
"""


class Empregado:
    def __init__(self, nome, departamento, horasTrabalhadasNoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasNoMes = horasTrabalhadasNoMes
        self.salarioPorHora = salarioPorHora

    def mostraDados(self):
        print(f"Nome: {self.nome}. Departamento: {self.departamento}. Horas Trabalhadas no mês: {self.horasTrabalhadasNoMes}. Salário/hora: {self.salarioPorHora}")

    def calculaSalarioMensal(self):
        salarioMensal = (self.salarioPorHora * self.horasTrabalhadasNoMes)
        print(f"Salário mensal {salarioMensal}")

