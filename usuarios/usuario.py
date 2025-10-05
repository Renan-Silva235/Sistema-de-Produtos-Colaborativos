class Usuario:

    def __init__(self, nivel, nome, idade, cpf, email, senha):
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
        self.nivel = nivel
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
            "nivel": self.nivel,
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "status": "ativo"
        }



class Solicitante(Usuario):
    def __init__(self, nivel, nome, idade, cpf, email, senha, endereco, cidade, estado, id_responsavel):
        """
        Inicializa um novo objeto do tipo Solicitante.

        :param nivel: O nível do usuário (Solicitante)
        :param nome: O nome do usuário
        :param idade: A idade do usuário
        :param cpf: O CPF do usuário
        :param email: O email do usuário
        :param senha: A senha do usuário
        :param Endereco: O endereço do usuário
        :param cidade: A cidade em que o usuário reside
        :param estado: O estado em que o usuário reside
        :param id_responsavel: O ID do responsável pelo usuário
        :return: None
        """
        super().__init__(nivel, nome, idade, cpf, email, senha)
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.id_responsavel = id_responsavel["id"]

    def objeto(self):
        """
        Retorna um dicionário contendo as informações do solicitante.

        :return: Um dicionário com as informações do solicitante.
        """
        dados = super().objeto()
        dados.update({
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "id_responsavel": self.id_responsavel,
            "status": "ativo"
        })

        return dados



