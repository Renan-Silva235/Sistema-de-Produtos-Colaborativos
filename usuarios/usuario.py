class PerfilUsuario:
    def __init__(self):
        self.administrador = "Administrador"
        self.atendente = "Atendente"
        self.entregador = "Entregador"

class Funcionario:

    def __init__(self, cargo, nome, idade, cpf, email, senha):
        """
        Inicializa um novo objeto do tipo Usuario.

        :param nivel: O nível do usuário (Administrador, Voluntário ou Solicitante)
        :param nome: O nome do usuário
        :param idade: A idade do usuário
        :param cpf: O CPF do usuário
        :param email: O email do usuário
        :param senha: A senha do usuário
        :return: None
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
            "status": "ativo"
        }



class Cliente:
    def __init__(self, nome, idade, cpf, email, senha, endereco, cidade, estado, id_responsavel):


        """
        Inicializa um novo objeto do tipo Cliente.

        :param nome: O nome do cliente
        :param idade: A idade do cliente
        :param cpf: O CPF do cliente
        :param email: O email do cliente
        :param senha: A senha do cliente
        :param endereco: O endereço do cliente
        :param cidade: A cidade em que o cliente reside
        :param estado: O estado em que o cliente reside
        :param id_responsavel: O ID do responsável pelo cliente
        :return: None
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
        Retorna um dicionário contendo as informações do solicitante.

        :return: Um dicionário com as informações do solicitante.
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
            "status": "ativo"
        }




