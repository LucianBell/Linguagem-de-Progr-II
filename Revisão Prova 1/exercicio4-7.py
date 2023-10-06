class Produto:
    def __init__(self, codigo, valor, descricao):
        self.__descricao = descricao
        self.__valor = valor
        self.__codigo = codigo

    def get_valor(self):
        return self.__valor


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.__quantidade = quantidade
        self.__custo = produto.get_valor() * self.__quantidade

    def mostrar(self):
        print(f"Custo do item pedido: {self.produto.get_valor() * self.__quantidade}")

    def get_custo(self):
        return self.__custo


class Pedido:
    def __init__(self):
        self.__valor_total = 0
        self.__itens = []

    def adicionar_item(self, item_pedido):
        self.__itens.append(item_pedido)
        self.__valor_total += item_pedido.get_custo()

    def obter_total(self):
        print(f"Custo total: {self.__valor_total}")


if __name__ == '__main__':
    # Criando produtos
    produto1 = Produto(1, 10.0, "Produto 1")
    produto2 = Produto(2, 20.0, "Produto 2")

    # Criando itens de pedido
    item1 = ItemPedido(produto1, 3)
    item2 = ItemPedido(produto2, 2)

    # Criando um pedido
    pedido = Pedido()

    # Adicionando itens ao pedido
    pedido.adicionar_item(item1)
    pedido.adicionar_item(item2)

    # Obtendo o total
    pedido.obter_total()