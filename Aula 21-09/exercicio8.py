class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'Valor do Ingresso: R$ {self.valor:.2f}')


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional


class Normal(Ingresso):
    def imprimeTipo(self):
        print('Ingresso Normal')


class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def imprimeLocalizacao(self):
        print(f'Localização: {self.localizacao}')


class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, localizacao_superior):
        super().__init__(valor, adicional)
        self.localizacao_superior = localizacao_superior

    def valorCamaroteSuperior(self):
        return self.valor + self.adicional

    def imprimeLocalizacaoSuperior(self):
        print(f'Localização: {self.localizacao_superior}')


if __name__ == '__main__':

    ingresso_normal = Normal(50)
    ingresso_normal.imprimeTipo()
    ingresso_normal.imprimeValor()

    ingresso_vip = VIP(100, 30)
    ingresso_vip.imprimeValor()
    valor_total_vip = ingresso_vip.valorVIP()
    print(f'Valor total do Ingresso VIP: R$ {valor_total_vip:.2f}')

    camarote_inferior = CamaroteInferior(80, 40, 'Setor A')
    camarote_inferior.imprimeLocalizacao()
    valor_total_camarote_inferior = camarote_inferior.valorVIP()
    print(f'Valor total do Camarote Inferior: R$ {valor_total_camarote_inferior:.2f}')

    camarote_superior = CamaroteSuperior(120, 60, 'Setor B - Superior')
    camarote_superior.imprimeLocalizacaoSuperior()
    valor_total_camarote_superior = camarote_superior.valorCamaroteSuperior()
    print(f'Valor total do Camarote Superior: R$ {valor_total_camarote_superior:.2f}')
