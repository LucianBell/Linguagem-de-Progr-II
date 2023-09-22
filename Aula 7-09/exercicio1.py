"""
Crie uma classe para conter os dados de cadastro de empregados de uma empresa chamada
CadastroEmpregado contendo: nome, idade, função na empresa, data de nascimento, telefone,
peso, altura e salário. Implemente as funções construtoras e as utilitárias que julgar necessário.
Desenvolva um programa que permita testar a funcionalidade da classe.
"""

class CadastroEmpregado:
    def __init__(self, nome, idade, funcao, data_nascimento, telefone, peso, altura, salario):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.peso = peso
        self.altura = altura
        self.salario = salario

    def atualizar_salario(self, novo_salario):
        self.salario = novo_salario

    def calcular_imc(self):
        altura_metros = self.altura / 100  # Converter altura para metros
        imc = self.peso / (altura_metros ** 2)
        return imc

    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Função na empresa:", self.funcao)
        print("Data de Nascimento:", self.data_nascimento)
        print("Telefone:", self.telefone)
        print("Peso (kg):", self.peso)
        print("Altura (cm):", self.altura)
        print("Salário:", self.salario)
        print("IMC:", self.calcular_imc())

# Programa de teste
if __name__ == "__main__":
    empregado1 = CadastroEmpregado("João Silva", 30, "Analista de Dados", "1993-05-15", "(11) 98765-4321", 75, 175, 5000.0)
    empregado2 = CadastroEmpregado("Maria Santos", 28, "Engenheira de Software", "1995-09-20", "(21) 12345-6789", 60, 160, 6000.0)

    # Mostrar informações iniciais dos empregados
    print("Informações iniciais do empregado 1:")
    empregado1.mostrar_informacoes()

    print("\nInformações iniciais do empregado 2:")
    empregado2.mostrar_informacoes()

    # Atualizar o salário do empregado 1
    empregado1.atualizar_salario(5500.0)

    # Mostrar informações atualizadas
    print("\nInformações atualizadas do empregado 1:")
    empregado1.mostrar_informacoes()