"""
Identifique as classes e implemente um programa para a seguinte especificação:
“O supermercado vende diferentes tipos de produtos. Cada produto tem um preço e uma quantidade em estoque.
Um pedido de um cliente é composto de itens, onde cada item especifica o produto que o cliente deseja e a
respectiva quantidade. Esse pedido pode ser pago em dinheiro, cheque ou cartão.”
"""

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} ({self.quantidade_estoque} em estoque)"

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self):
        self.itens = []
        self.metodo_pagamento = None

    def adicionar_item(self, item):
        self.itens.append(item)

    def definir_metodo_pagamento(self, metodo):
        self.metodo_pagamento = metodo

    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self.itens)
        return total

class Supermercado:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def realizar_pedido(self, pedido):
        for item in pedido.itens:
            if item.produto in self.produtos:
                produto = item.produto
                if produto.quantidade_estoque >= item.quantidade:
                    produto.quantidade_estoque -= item.quantidade
                else:
                    print(f"Estoque insuficiente para {produto.nome}")
            else:
                print(f"Produto {item.produto.nome} não disponível")

    def processar_pagamento(self, pedido):
        if pedido.metodo_pagamento == "dinheiro":
            print(f"Pagamento em dinheiro no valor de R${pedido.calcular_total():.2f} aceito.")
        elif pedido.metodo_pagamento == "cheque":
            print("Pagamento com cheque aceito.")
        elif pedido.metodo_pagamento == "cartao":
            print("Pagamento com cartão aceito.")
        else:
            print("Método de pagamento não reconhecido.")

# Programa de teste
if __name__ == "__main__":
    supermercado = Supermercado()

    # Adicionar produtos ao inventário do supermercado
    produto1 = Produto("Arroz", 5.0, 100)
    produto2 = Produto("Feijão", 3.5, 50)
    supermercado.adicionar_produto(produto1)
    supermercado.adicionar_produto(produto2)

    # Criar um pedido
    pedido1 = Pedido()
    item1 = ItemPedido(produto1, 2)
    item2 = ItemPedido(produto2, 3)
    pedido1.adicionar_item(item1)
    pedido1.adicionar_item(item2)
    pedido1.definir_metodo_pagamento("dinheiro")

    # Processar o pedido
    supermercado.realizar_pedido(pedido1)

    # Processar o pagamento
    supermercado.processar_pagamento(pedido1)

    # Exibir informações do pedido
    print("Itens do pedido:")
    for item in pedido1.itens:
        print(f"{item.quantidade}x {item.produto.nome} - Subtotal: R${item.calcular_subtotal():.2f}")
    print(f"Total do pedido: R${pedido1.calcular_total():.2f}")