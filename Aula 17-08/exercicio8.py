"""
Crie um modelo Musica para representar uma música, para uso em uma coleção ou banco de dados de músicas.
Que atributos e operações esse modelo deve ter?
"""


class Musica:
    def __init__(self, titulo, artista, album, duracao_em_segundas, genero, avaliacao):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao_em_segundos = duracao_em_segundas
        self.genero = genero
        self.avaliacao = avaliacao

    def reproduzir(self):
        print(f"Reproduzindo '{self.titulo}' de {self.artista}")

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Album: {self.album}")
        print(f"Duração: {self.duracao_em_segundos}")
        print(f"Gênero: {self.genero}")
        print(f"Avaliação: {self.avaliacao}")


minha_musica = Musica("Bohemian Rhapsody", "Queen", "A Night at the Opera", 355, "Rock", 10)
minha_musica.reproduzir()
minha_musica.mostrar_info()
