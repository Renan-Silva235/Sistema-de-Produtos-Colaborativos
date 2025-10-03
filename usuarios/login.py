from crud.crud import Crud
class Login:
    def __init__(self, arquivo):
        """O construtor recebe o arquivo json que será manipulado"""
        self.arquivo = arquivo


    def autenticar(self, nivel, email, senha):
        """Esse método recebe email e senha para fazer login no sistema"""
        dados = Crud(self.arquivo).listar()
        for dado in dados:
            if dado["nivel"] == nivel and dado["email"] == email and dado["senha"] == senha:
                return dado

        return False








