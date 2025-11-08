class PerfilUsuario:
    """
    Classe que define os perfis de usuário do sistema.

    Armazena constantes com os nomes dos cargos disponíveis no sistema.
    """

    def __init__(self):
        """
        Inicializa um objeto PerfilUsuario com os cargos disponíveis.
        """
        self.administrador = "Administrador"
        self.atendente = "Atendente"
        self.entregador = "Entregador"

class Funcionario:
    """
    Classe que representa um funcionário do sistema.

    Armazena informações sobre funcionários (Administrador, Atendente ou Entregador).
    """

    def __init__(self, cargo, nome, idade, cpf, email, senha):
        """
        Inicializa um novo objeto do tipo Funcionario.

        :param cargo: String com o cargo do funcionário (Administrador, Atendente ou Entregador)
        :param nome: String com o nome do funcionário
        :param idade: Inteiro com a idade do funcionário
        :param cpf: String com o CPF do funcionário
        :param email: String com o email do funcionário
        :param senha: String com a senha do funcionário
        """
        self.cargo = cargo
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.senha = senha


    def objeto(self):
        """
        Retorna um dicionário contendo as informações do usuário.

        :return: Um dicionário com as informações do usuário.
        """
        return {
            "cargo": self.cargo,
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "email": self.email,
            "senha": self.senha,
        }



class Cliente:
    """
    Classe que representa um cliente (solicitante) do sistema.

    Armazena informações sobre clientes que solicitam produtos doados.
    """

    def __init__(self, nome, idade, cpf, email, senha, endereco, cidade, estado, id_responsavel):
        """
        Inicializa um novo objeto do tipo Cliente.

        :param nome: String com o nome do cliente
        :param idade: Inteiro com a idade do cliente
        :param cpf: String com o CPF do cliente
        :param email: String com o email do cliente
        :param senha: String com a senha do cliente
        :param endereco: String com o endereço do cliente
        :param cidade: String com a cidade em que o cliente reside
        :param estado: String com o estado em que o cliente reside
        :param id_responsavel: Dicionário com os dados do responsável (utiliza o campo 'id')
        """
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.id_responsavel = id_responsavel["id"]

    def objeto(self):
        """
        Retorna um dicionário contendo as informações do cliente formatadas para armazenamento.

        :return: Dicionário com os dados do cliente, incluindo status "ativo"
        """
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "id_responsavel": self.id_responsavel,
        }
