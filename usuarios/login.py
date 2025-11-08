from crud.crud import Crud


class Login:
    """
    Classe responsável por autenticação de usuários no sistema.

    Fornece métodos para verificar credenciais de login (email e senha).
    """

    def __init__(self, arquivo):
        """
        Inicializa um objeto Login com o arquivo JSON que contém os usuários.

        :param arquivo: String com o caminho do arquivo JSON de usuários
        """
        self.arquivo = arquivo


    def autenticar(self, email, senha):
        """
        Realiza a autenticação de um usuário com base nos dados do JSON.

        :param email: String com o e-mail do usuário
        :param senha: String com a senha do usuário
        :return: Dicionário com os dados do usuário se a autenticação for bem-sucedida,
                 False caso contrário
        """
        dados = Crud(self.arquivo).listar()
        for dado in dados:
            if dado["email"] == email and dado["senha"] == senha:
                return dado

        return False
