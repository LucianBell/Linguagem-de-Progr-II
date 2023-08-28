"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio.
A classe deve armazenar o andar atual (0=térreo), total de andares no prédio, excluindo o térreo,
capacidade do elevador, e quantas pessoas estão presentes nele.A classe deve também disponibilizar os
seguintes métodos:

inicializa: que deve receber como parâmetros: a capacidade do elevador e o total de andares no prédio
(os elevadores sempre começam no térreo e vazios);

entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
sobe: para subir um andar (não deve subir se já estiver no último andar);
desce: para descer um andar (não deve descer se já estiver no térreo);
get....: métodos para obter cada um dos os dados armazenados.
"""


class Elevador:
    def __init__(self, total_de_andares, capacidade):
        self.total_de_andares = total_de_andares
        self.capacidade = capacidade
        self.andar_atual = 0
        self.pessoas_presentes = 0

    def entra(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
            print("Uma pessoa entrou no elevador")
        else:
            print("Operação inválida. Capacidade máxima atingida.")

    def sai(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
            print("Uma pessoa saiu do elevador")
        else:
            print("Operação inválida. Não há ninguém no elevador.")

    def sobe(self):
        if self.andar_atual < self.total_de_andares:
            self.andar_atual += 1
            print("O elevador subiu um andar")
        else:
            print("Operação inválida. Elevador está no último andar.")

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("O elevador desceu um andar")
        else:
            print("Operação inválida. Elevador está no térreo.")

    def get_andaratual(self):
        print(f"Andar atual: {self.andar_atual}")

    def get_andares(self):
        print(f"Total de andares: {self.total_de_andares}")

    def get_capacidade(self):
        print(f"Capacidade total: {self.capacidade}")

    def get_pessoas(self):
        print(f"Quantidade de pessoas presentes: {self.pessoas_presentes}")


if __name__ == '__main__':
    elevador = Elevador(5, 10)

    elevador.sobe()
    elevador.entra()
    elevador.entra()
    elevador.sai()
    elevador.sobe()
    elevador.sobe()
    elevador.sobe()
    elevador.sobe()
    elevador.sobe()
    elevador.get_capacidade()
    elevador.get_andares()
    elevador.get_andaratual()
    elevador.get_pessoas()
