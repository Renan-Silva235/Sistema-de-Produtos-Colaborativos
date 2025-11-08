from crud.crud import Crud
from utils.sistema.sistema import Sistema


class Doador:
    """
    Classe que representa um doador do sistema.

    Armazena informações sobre doadores que realizam doações de produtos.
    """
    def __init__(self, nome, idade, cpf, telefone, email, cidade, estado, id_responsavel):
        """
        Inicializa um novo objeto do tipo Doador.

        :param nome: O nome do doador
        :param idade: A idade do doador
        :param cpf: O CPF do doador
        :param telefone: O telefone do doador
        :param email: O email do doador
        :param cidade: A cidade em que o doador reside
        :param estado: O estado em que o doador reside
        :param id_responsavel: O ID do responsável pelo doador
        :return: None
        """
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.cidade = cidade
        self.estado = estado
        self.id_responsavel = id_responsavel
        self.total_doacoes = 0


    def objeto(self):
        """
        Retorna um dicionário contendo as informações do doador.

        :return: Um dicionário com as informações do doador.
        """
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email":self.email,
            "cidade": self.cidade,
            "estado": self.estado,
            "id_responsavel": self.id_responsavel,
            "total_doacoes": self.total_doacoes,

        }


class Doacao:
    """
    Classe que representa uma doação realizada no sistema.

    Armazena informações sobre a doação, incluindo o doador, produto e responsável.
    """

    def __init__(self, id_doador: Doador, produto: dict, id_responsavel: Crud):
        """
        Inicializa um novo objeto do tipo Doacao.

        :param id_doador: Dicionário com os dados do doador (utiliza o campo 'id')
        :param produto: Dicionário contendo as informações do produto doado
        :param id_responsavel: Dicionário com os dados do responsável (utiliza o campo 'id')
        """
        self.id_doador = id_doador["id"]
        self.produto = produto
        self.id_responsavel = id_responsavel["id"]

    def objeto(self):
        """
        Retorna um dicionário contendo as informações da doação.

        :return: Um dicionário com as informações da doação.
        """
        dados = self.produto
        dados.update({
            "id_doador": [self.id_doador],
            "id_responsavel":[self.id_responsavel],
            "status": "ativo",
            "data_registrada": Sistema.data_hora_atual()
        })

        return dados
