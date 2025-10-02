from crud.crud import Crud
class Doador:
    def __init__(self, nome, idade, cpf, telefone, email, cidade, estado, id_responsavel):
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

        self.id_doador = id_doador["id"]
        self.produto = produto
        self.id_responsavel = id_responsavel["id"]

    def objeto(self):
        dados = self.produto
        dados.update({
            "id_doador": [self.id_doador],
            "id_responsavel":[self.id_responsavel],
        })

        return dados



