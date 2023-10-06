"""
Implemente uma televisão. A televisão tem um controle de volume do som e um controle de seleção de canal.
O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez.
O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém,
também possibilita trocar para um canal indicado.
Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.
No programa principal, crie uma televisão e troque de canal algumas vezes. Aumente um pouco o volume,
e exiba o valor de ambos os atributos.
"""


class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 0

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado")
        else:
            print("Volume máximo: 100")

    def baixar_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume abaixado")
        else:
            print("Volume minimo: 0")

    def trocar_canal(self, canal_novo):
        if canal_novo < 100 and canal_novo > 0:
            self.canal = canal_novo
            print(f"Canal atual: {self.canal}")
        else:
            print("Error: insira um canal válido")