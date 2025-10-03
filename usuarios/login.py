from crud.crud import Crud
class Login:
    def __init__(self, arquivo):
        """O construtor recebe o arquivo json que será manipulado"""
        self.arquivo = arquivo


    def autenticar(self, nivel, email, senha):

        """
        Realiza a autenticação de um usuário com base nos dados do json

        :param nivel: O nível do usuário
        :param email: O e-mail do usuário
        :param senha: A senha do usuário
        :return: O dicionário do usuário se a autenticação for bem sucedida, False caso contrário
        """
        dados = Crud(self.arquivo).listar()
        for dado in dados:
            if dado["nivel"] == nivel and dado["email"] == email and dado["senha"] == senha:
                return dado

        return False








