"""
Crie uma classe Agenda que armazena 10 pessoas e seja capaz de operações como:

...
"""


class Agenda:
    def __init__(self):
        self.pessoas = []

    def armazena_pessoa(self, nome, idade, altura):
        if len(self.pessoas) < 10:
            pessoa = {
                "nome": nome,
                "idade": idade,
                "altura": altura
            }
            self.pessoas.append(pessoa)
            print(f"{pessoa['nome']} foi adicionada a lista de contatos")
        else:
            print("Error: limite de contatos atingido")

    def busca_pessoa(self, nome_buscado):
        verificador = 0

        if len(self.pessoas) > 0:
            for i, pessoa in enumerate(self.pessoas):
                if pessoa["nome"] == nome_buscado:
                    print(f"{nome_buscado} está na agenda na posição {(i + 1)}")
                    verificador += 1

            if verificador == 0:
                print("Contato não encontrado")

    def imprime_agenda(self):
        for i, pessoa in enumerate(self.pessoas):
            print(f"Contato {i + 1}: {pessoa['nome']}.")

    def imprime_pessoa(self, index):
        if len(self.pessoas) >= index:
            pessoa = self.pessoas[(index - 1)]
            print(f"Contato na posição {index}: {pessoa['nome']}")
        else:
            print("Você não tem nenhum contato nessa posição da agenda.")


if __name__ == '__main__':
    agenda = Agenda()

    agenda.armazena_pessoa("João", 30, 1.80)
    agenda.armazena_pessoa("Maria", 25, 1.65)
    agenda.armazena_pessoa("Pedro", 40, 1.75)
    agenda.armazena_pessoa("Ana", 35, 1.70)
    agenda.armazena_pessoa("Carlos", 28, 1.90)

    agenda.imprime_agenda()

    agenda.busca_pessoa("Maria")
    agenda.busca_pessoa("Lucas")

    agenda.imprime_pessoa(2)
    agenda.imprime_pessoa(5)
