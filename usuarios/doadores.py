from crud.crud import Crud
class Doador:
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
            "total_doacoes": self.total_doacoes
        }


class Doacao:
    def __init__(self, id_doador: Doador, produto: dict, id_responsavel: Crud):

        """
        Inicializa um novo objeto do tipo Doacao.

        :param id_doador: O id do doador que realizou a doacao
        :param produto: Um dicionario contendo as informacoes do produto doado
        :param id_responsavel: O id do responsavel pela doacao
        :return: None
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
        })

        return dados



