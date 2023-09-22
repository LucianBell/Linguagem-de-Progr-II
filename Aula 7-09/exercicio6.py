"""
Crie um programa para representar funcionarios em um sistema de gestao de pessoas.

É necessario que nesta modelagem seja feito de uso de no minimo duas classes e com uma associacao entre estas.
Cada classe deverá ter no mínimo 2 atributos.


<<Possível resposta - O arquivo Main.py é o principal>>
"""

class Departamento:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return f"Departamento: {self.nome}, Código: {self.codigo}"


class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def __str__(self):
        return f"Nome: {self.nome}, Salário: R${self.salario:.2f}, {self.departamento}"


if __name__ == "__main__":
    # Criar departamentos
    rh = Departamento("Recursos Humanos", "RH101")
    ti = Departamento("Tecnologia da Informação", "TI202")

    # Criar funcionários e associá-los aos departamentos
    funcionario1 = Funcionario("João", 5000.0, rh)
    funcionario2 = Funcionario("Maria", 6000.0, ti)

    # Aumentar o salário de funcionário1 em 10%
    funcionario1.aumentar_salario(10)

    # Exibir informações dos funcionários e departamentos
    print(funcionario1)
    print(funcionario2)