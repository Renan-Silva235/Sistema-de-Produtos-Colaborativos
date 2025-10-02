class Alimentos:
    def __init__(self, nome_alimento, peso, validade, quantidade):
        self.nome_alimento = nome_alimento
        self.peso = peso
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        return {
            "categoria": "Alimentícios",
            "nome_alimento": self.nome_alimento,
            "peso": self.peso,
            "validade": self.validade,
            "quantidade": self.quantidade
        }


class Medicamentos:
    def __init__(self, nome_medicamento, dosagem, validade, quantidade):
        self.nome_medicamento = nome_medicamento,
        self.dosagem = dosagem
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        return {
            "categoria": "Medicamentos",
            "nome_medicamento": self.nome_medicamento,
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
            "categoria": "Vestuário",
            "nome_produto": self.nome_produto,
            "marca": self.marca,
            "cor": self.cor,
            "tamanho": self.tamanho,
            "quantidade": self.quantidade
        }


