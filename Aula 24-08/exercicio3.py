"""
Crie uma classe Agenda que armazena 10 pessoas e seja capaz de operações como:
class Agenda:
    pessoa Pessoa[10];

    armazenaPessoa(nome, idade, altura);
    buscaPessoa(string nome); // informa em que posição da agenda está a pessoa
    imprimeAgenda(); // imprime todos os dados de todas as pessoas da agenda
    imprimePessoa(int i); // imprime os dados da pessoa que está na posição 'i' da agenda


if __name__ == "main":
    a = Agenda();
    // faça aqui o teste da agenda.
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
            print("Pessoa adicionada a agenda")
        else:
            print("Não é possível adicionar mais pessoas a agenda")

    def busca_pessoa(self, nome_buscado):
        verificador = 0

        for i, pessoa in enumerate(self.pessoas):
            if pessoa["nome"] == nome_buscado:
                print(f"{nome_buscado} está na posição {(i + 1)}")
                verificador += 1

        if verificador == 0:
            print(f"Pessoa com nome {nome_buscado} não foi encontrada na agenda")

    def imprime_agenda(self):
        print("\nAgenda")
        for i, pessoa in enumerate(self.pessoas):
            print(f"{i}. Nome: {pessoa['nome']}. Idade: {pessoa['idade']}. Altura: {pessoa['altura']}")

    def imprime_pessoa(self, posicao):
        print(f"Pessoa na posição {posicao}: {self.pessoas[(posicao - 1)]}")


if __name__ == '__main__':
    agenda = Agenda()

    agenda.armazena_pessoa("João", 25, 1.75)
    agenda.armazena_pessoa("Maria", 30, 1.65)
    agenda.armazena_pessoa("Carlos", 40, 1.80)
    agenda.armazena_pessoa("Ana", 28, 1.70)

    agenda.busca_pessoa("Maria")

    agenda.imprime_agenda()
    agenda.imprime_pessoa(2)
