"""
Seja o trecho de programa Caixa

minhaConta = Conta();
minhaConta.deposita(100 );
minhaConta.setLimite(100 );
minhaConta.saca(1000 );

Suponha que o método saca da classe Conta vai ser rescrito de forma a lançar uma exceção criada por voce cuja classe
é ContaExceção. A exceção é lançada sempre que o saldo da conta for negativo. Implemente a classe ContaExceção.
Implemente o método saca que lança a exceção. E rescreva o código caixa com o devido tratamento da exceção.
"""


class ContaExcecao(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Conta:
    def __init__(self):
        self.saldo = 0
        self.limite = 0

    def deposita(self, valor):
        self.saldo += valor

    def setLimite(self, limite):
        self.limite = limite

    def saca(self, valor):
        if valor > self.saldo + self.limite:
            raise ContaExcecao("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor


# Código "Caixa" com tratamento de exceção
try:
    minhaConta = Conta()
    minhaConta.deposita(100)
    minhaConta.setLimite(100)
    minhaConta.saca(1000)
except ContaExcecao as ce:
    print("Erro:", ce)
