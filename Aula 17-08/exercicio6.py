"""
Crie um modelo para representar um time de um esporte qualquer em um campeonato desse esporte.
Que atributos e operações esse modelo deve ter?
"""


class TimeBasqueteNBA:
    def __init__(self, nome, divisao, cidade, posicao_ranking, jogadores):
        if not isinstance(jogadores, list):
            raise ValueError("O parâmetro 'jogadores' deve ser uma lista de strings")

        for jogador in jogadores:
            if not isinstance(jogador, str):
                raise ValueError("Os elementos da lista 'materia' devem ser strings")

        self.nome = nome
        self.divisao = divisao
        self.cidade = cidade
        self.posicao_ranking = posicao_ranking
        self.jogadores = jogadores

    def adicionar_jogador(self, jogador_novo):
        self.jogadores.append(jogador_novo)
        return f"Lista de jogadores atualizada. Novo Jogador: {jogador_novo}"

    def remover_jogador(self, jogador_removido):
        self.jogadores.remove(jogador_removido)
        return f"Lista de jogadores atualizada. Jogador removido: {jogador_removido}"

    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(jogador)

    def esta_nos_playoffs(self):
        if self.posicao_ranking <= 8:
            return True
        else:
            return False

    def mostrar_infos(self):
        print(f"Time: {self.nome}")
        print(f"Divisão: {self.divisao}")
        print(f"Cidade: {self.cidade}")
        print(f"Posição no Ranking: {self.posicao_ranking}")
        print(f"Está nos playoffs? {self.esta_nos_playoffs()}")
        print("Jogadores:")
        self.listar_jogadores()


jogadores_time = ["Jogador1", "Jogador2", "Jogador3"]
time = TimeBasqueteNBA("Time Teste", "Conferência Leste", "Cidade Teste", 5, jogadores_time)

print(time.nome)
time.listar_jogadores()
print(time.adicionar_jogador("Jogador4"))
time.listar_jogadores()
print(time.remover_jogador("Jogador2"))
print(time.esta_nos_playoffs())
time.mostrar_infos()
