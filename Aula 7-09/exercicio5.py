"""
Faça uma programa para representar a árvore genealógica de uma família.
Para tal, crie uma classe Pessoa que permita indicar, além de nome e idade, o pai e a mãe.
Tenha em mente que pai e mãe também são do tipo Pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade, pai=None, mae=None):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae

    def adicionar_filho(self, filho):
        if filho:
            if filho not in self.filhos():
                if self.pai is None:
                    self.pai = filho
                elif self.mae is None:
                    self.mae = filho
                else:
                    print(f"{self.nome} já tem pai e mãe definidos.")
            else:
                print(f"{filho.nome} já é filho de {self.nome}.")
        else:
            print("Filho não válido.")

    def filhos(self):
        filhos = []
        if self.pai:
            filhos.append(self.pai)
        if self.mae:
            filhos.append(self.mae)
        return filhos

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Pai: {self.pai.nome if self.pai else 'N/A'}, Mãe: {self.mae.nome if self.mae else 'N/A'}"


# Função para exibir a árvore genealógica recursivamente
def exibir_arvore(pessoa, nivel=0):
    espacos = "  " * nivel
    print(f"{espacos}{pessoa.nome}")
    for filho in pessoa.filhos():
        exibir_arvore(filho, nivel + 1)


# Exemplo de construção da árvore genealógica
if __name__ == "__main__":
    avo_paterno = Pessoa("Avo Paterno", 70)
    avo_materno = Pessoa("Avo Materno", 75)
    pai = Pessoa("Pai", 40, avo_paterno, avo_materno)
    mae = Pessoa("Mae", 38)
    filho1 = Pessoa("Filho 1", 15, pai, mae)
    filho2 = Pessoa("Filho 2", 12, pai, mae)

    # Adicionando filho diretamente
    avo_paterno.adicionar_filho(pai)
    avo_materno.adicionar_filho(pai)
    pai.adicionar_filho(filho1)
    pai.adicionar_filho(filho2)

    # Exibindo a árvore genealógica
    exibir_arvore(avo_paterno)