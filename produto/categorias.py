class Alimentos:
    """
    Classe que representa um produto da categoria Alimentícios.

    Armazena informações sobre alimentos doados, incluindo nome, peso, validade e quantidade.
    """

    def __init__(self, nome_alimento, peso, validade, quantidade):
        """
        Inicializa um novo objeto do tipo Alimentos.

        :param nome_alimento: String com o nome do alimento
        :param peso: String com o peso do alimento (ex: "500g", "1.5kg")
        :param validade: String com a data de validade no formato dd/mm/aaaa
        :param quantidade: Inteiro com a quantidade de unidades do produto
        """
        self.nome_alimento = nome_alimento
        self.peso = peso
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        """
        Retorna um dicionário contendo as informações do alimento formatadas para armazenamento.

        :return: Dicionário com os dados do alimento, incluindo a categoria "Alimentícios"
        """
        return {
            "categoria": "Alimentícios",
            "nome_alimento": self.nome_alimento,
            "peso": self.peso,
            "validade": self.validade,
            "quantidade": self.quantidade
        }


class Medicamentos:
    """
    Classe que representa um produto da categoria Medicamentos.

    Armazena informações sobre medicamentos doados, incluindo nome, dosagem, validade e quantidade.
    """

    def __init__(self, nome_medicamento, dosagem, validade, quantidade):
        """
        Inicializa um novo objeto do tipo Medicamentos.

        :param nome_medicamento: String com o nome do medicamento
        :param dosagem: String com a dosagem do medicamento (ex: "500mg", "100mg")
        :param validade: String com a data de validade no formato dd/mm/aaaa
        :param quantidade: Inteiro com a quantidade de unidades do medicamento
        """
        self.nome_medicamento = nome_medicamento
        self.dosagem = dosagem
        self.validade = validade
        self.quantidade = quantidade

    def objeto(self):
        """
        Retorna um dicionário contendo as informações do medicamento formatadas para armazenamento.

        :return: Dicionário com os dados do medicamento, incluindo a categoria "Medicamentos"
        """
        return {
            "categoria": "Medicamentos",
            "nome_medicamento": self.nome_medicamento,
            "dosagem": self.dosagem,
            "validade": self.validade,
            "quantidade": self.quantidade
        }


class Vestuario:
    """
    Classe que representa um produto da categoria Vestuário.

    Armazena informações sobre roupas e calçados doados, incluindo nome, marca, cor, tamanho e quantidade.
    """

    def __init__(self, nome_produto, marca, cor, tamanho, quantidade):
        """
        Inicializa um novo objeto do tipo Vestuario.

        :param nome_produto: String com o nome do produto (ex: "Meia", "Blusa", "Calça")
        :param marca: String com a marca do produto
        :param cor: String com a cor do produto
        :param tamanho: String com o tamanho (P, M, G, GG para roupas ou números para calçados)
        :param quantidade: Inteiro com a quantidade de unidades do produto
        """
        self.nome_produto = nome_produto
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.quantidade = quantidade

    def objeto(self):
        """
        Retorna um dicionário contendo as informações do vestuário formatadas para armazenamento.

        :return: Dicionário com os dados do vestuário, incluindo a categoria "Vestuário"
        """
        return {
            "categoria": "Vestuário",
            "nome_produto": self.nome_produto,
            "marca": self.marca,
            "cor": self.cor,
            "tamanho": self.tamanho,
            "quantidade": self.quantidade
        }


