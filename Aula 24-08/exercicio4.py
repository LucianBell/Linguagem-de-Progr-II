"""
Implemente uma televisão. A televisão tem um controle de volume do som e um controle de seleção de canal.
O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez.
O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também
possibilita trocar para um canal indicado. Também devem existir métodos para consultar o valor do volume
de som e o canal selecionado. No programa principal, crie uma televisão e troque de canal algumas vezes.
Aumente um pouco o volume, e exiba o valor de ambos os atributos.
"""


class Televisao:
    def __init__(self, volume, canal):
        self.volume = volume
        self.canal = canal

    def aumentar_volume(self):
        if self.volume == 100:
            print("Volume max: 100. Operação não permitida")
        else:
            self.volume = (self.volume + 1)
            print(f"Novo volume: {self.volume}")

    def diminuir_volume(self):
        if self.volume == 0:
            print("Volume zerado. Operação não permitida")
        else:
            self.volume = (self.volume - 1)
            print(f"Novo volume: {self.volume}")

    def aumentar_canal(self):
        if self.canal == 100:
            print("Operação não permitida")
        else:
            self.canal = (self.canal + 1)
            print(f"Novo canal: {self.canal}")

    def diminuir_canal(self):
        if self.canal == 0:
            print("Operação não permitida")
        else:
            self.canal = (self.canal - 1)
            print(f"Novo canal: {self.canal}")

    def escolher_canal(self, canal_escolhido):
        if canal_escolhido > 100 or canal_escolhido < 0:
            print("Operação não permitida")
        else:
            self.canal = canal_escolhido
            print(f"Novo canal: {self.canal}")

    def mostrar_dados(self):
        print("CONFIGURAÇÕES ATUAIS:")
        print(f"Canal atual: {self.canal}")
        print(f"Volume atual: {self.volume}\n")


if __name__ == '__main__':

    televisao = Televisao(50, 5)

    televisao.aumentar_canal()
    televisao.aumentar_canal()
    televisao.aumentar_canal()

    televisao.aumentar_volume()
    televisao.mostrar_dados()

    televisao.escolher_canal(10)
    televisao.mostrar_dados()
