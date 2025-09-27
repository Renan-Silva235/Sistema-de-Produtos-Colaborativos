class Alimentos:
    def __init__(self, nome_alimento, peso, validade, quantidade):
        self.nome_alimento = nome_alimento
        self.peso = peso
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        return {
            "nome_alimento": self.nome_alimento,
            "peso": self.peso,
            "validade": self.validade,
            "quantidade": self.quantidade
        }


class Medicamentos:
    def __init__(self, nome_comercial, nome_generico, categoria, apresentacao, dosagem, validade, quantidade):
        self.nome_comercial = nome_comercial,
        self.nome_generico = nome_generico
        self.categoria = categoria
        self.apresentacao = apresentacao
        self.dosagem = dosagem
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        return {
            "nome_comercial": self.nome_comercial,
            "nome_generico": self.nome_generico,
            "categoria": self.categoria,
            "apresentacao": self.apresentacao,
            "dosagem": self.dosagem,
            "validade": self.validade,
            "quantidade": self.quantidade
        }


class Vestuario:
    def __init__(self, nome_produto, marca, cor, tamanho, quantidade):
        self.nome_produto = nome_produto
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.quantidade = quantidade


    def objeto(self):
        return {
            "nome_produto": self.nome_produto,
            "marca": self.marca,
            "cor": self.cor,
            "tamanho": self.tamanho,
            "quantidade": self.quantidade
        }


