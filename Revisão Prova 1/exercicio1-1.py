"""
Escreva um modelo para representar uma lâmpada que está à venda em um supermercado.
Que atributos devem ser representados por este modelo?
"""


class Lampada:
    def __init__(self, valor, voltagem, cor):
        self.valor = valor
        self.voltagem = voltagem
        self.cor = cor
        self.estado = "desligada"

    def ligar_ou_desligar(self):
        if self.estado == "desligada":
            self.estado = "ligada"
            print("Lâmpada ligada")
        else:
            self.estado = "desligada"
            print("Lâmpada desligada")

