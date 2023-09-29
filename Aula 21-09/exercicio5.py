"""
Implemente a classe Funcionario e a classe Gerente.

crie a classe Assistente, que também é um funcionário, e que possui um número de matrícula (faça o método GET).
Sobrescreva o método exibeDados().
sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos possuem um
turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo.
"""


class Funcionario:
    def __init__(self, nome, cargo, idade, salario):
        self.nome = nome
        self.cargo = cargo
        self.idade = idade
        self.salario = salario

    def respirar(self):
        print("Respirando...")

    def mostrar_dados(self):
        print(f"Nome: {self.nome}; Idade: {self.idade}; Cargo: {self.cargo}; Salario: {self.salario}")


class Gerente:
    def __init__(self, nome, xp, idade, salario):
        self.nome = nome
        self.xp = xp
        self.idade = idade
        self.salario = salario

    def mostrar_dados(self):
        print(f"Nome: {self.nome}; Idade: {self.idade}; Anos de experiência: {self.xp}; Salario: {self.salario}")

    def gerenciar(self):
        print(f"Gerente {self.nome} está gerenciando...")


class Assistente(Funcionario):
    def __init__(self, nome, cargo, idade, salario, numero_matricula):
        super().__init__(nome, cargo, idade, salario)
        self.numero_matricula = numero_matricula

    def get_numero_matricula(self):
        print(f"Numero de matricula: {self.numero_matricula}")

    def mostrar_dados(self):
        super().mostrar_dados()
        self.get_numero_matricula()


class AssistenteTecnico(Assistente):
    def __init__(self, nome, cargo, idade, salario, numero_matricula, bonus_salarial):
        super().__init__(nome, cargo, idade, salario, numero_matricula)
        self.bonus_salarial = bonus_salarial
        self.salario = salario + bonus_salarial

    def get_bonus_salarial(self):
        print(f"Bonus salaria: {self.bonus_salarial}")

    def mostrar_dados(self):
        super().mostrar_dados()
        self.get_bonus_salarial()


class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, cargo, idade, salario, numero_matricula, turno, adicional_noturno):
        super().__init__(nome, cargo, idade, salario, numero_matricula)
        self.turno = turno
        if turno == "noite":
            self.salario += adicional_noturno
            self.adicional_noturno = adicional_noturno

    def mostrarbonus_noturno(self):
        if turno == "noite":
            print(f"Bonus noturno: {self.adicional_noturno}")
        else:
            print("Sem adicional noturno.")

    def mostrar_dados(self):
        super().mostrar_dados()
        self.mostrarbonus_noturno()
