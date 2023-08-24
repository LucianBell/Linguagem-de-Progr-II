"""
Crie um modelo Livro que represente os atributos básicos de um livro, sem se preocupar com a sua finalidade
"""


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, editora, avaliacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.editora = editora
        self.avaliaco = avaliacao

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Editora: {self.editora}")
        print(f"Nota: {self.avaliaco}")


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, "Editora A", 9)

livro1.mostrar_informacoes()
