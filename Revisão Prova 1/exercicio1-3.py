"""
Imagine uma lâmpada que possa ter três estados: apagada, acesa e meia-luz. Escreva o modelo (classe)
LampadaTresEstados


Generalize o modelo LampadaTresEstados para que ele possa representar uma lâmpada onde a
luminosidade pode ser ajustada com qualquer valor entre 0% (apagada) e 100% (acesa).
Dica: em vez de operações para possibilitar o ajuste para cada um dos estados,
descreva uma operação que receba um valor de ajuste.
"""


class LampadaTresEstados:
    def __init__(self):
        self.estado = "apagada"
        self.luminosidade = 0

    def deixar_apagada(self):
        self.estado = "apagada"
        self.luminosidade = 0
        print("Lâmpada apagada")

    def deixar_acesa(self):
        self.estado = "acesa"
        self.luminosidade = 100

    def deixar_meia_luz(self):
        self.estado = "meia-luz"
        self.luminosidade = 50

    def ajustar_luminosidade(self, valor):
        if valor > 100:
            print("Error: valor máximo == 100")
            self.luminosidade = 100
            self.estado = "ligada"
        elif valor < 0:
            print("Error: valor minimo == 100")
            self.luminosidade = 0
            self.estado = "desligada"
        else:
            self.luminosidade = valor
            self.estado = "ligada com valor ajustado"
            print(f"Luminosidade com valor {self.luminosidade}")
