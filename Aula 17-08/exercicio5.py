"""
Crie um modelo para representar um professor de uma disciplina qualquer
"""


class Professor:
    def __init__(self, nome_completo, materias, escolaridade, nivel_de_dificuldade, nivel_de_loucura):
        if not isinstance(materias, list):
            raise ValueError("O parâmetro 'materia' deve ser uma lista de strings")

        for item in materias:
            if not isinstance(item, str):
                raise ValueError("Os elementos da lista 'materia' devem ser strings")

        self.nome_completo = nome_completo
        self.materias = materias
        self.escolaridade = escolaridade
        self.nivel_de_dificuldade = nivel_de_dificuldade
        self.nivel_de_loucura = nivel_de_loucura

    def mostrar_nome_escolaridade_materia(self):
        return f"Nome: {self.nome_completo}. Escolaridade: {self.escolaridade}. Materia Principal: {self.materias[0]}"


professorImaginario = Professor("Nome Falso", ["Math I", "Math II"], "PhD", 9, 10)
print(professorImaginario.mostrar_nome_escolaridade_materia())
