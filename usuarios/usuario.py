class Usuario:

    def __init__(self, nivel, nome, idade, cpf, email, senha):
        self.nivel = nivel
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.senha = senha


    def objeto(self):
        return {
            "nivel": self.nivel,
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "email": self.email,
            "senha": self.senha
        }



class Solicitante(Usuario):
    def __init__(self, nivel, nome, idade, cpf, email, senha, endereco, cidade, estado, id_responsavel):
        super().__init__(nivel, nome, idade, cpf, email, senha)
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.id_responsavel = id_responsavel["id"]

    def objeto(self):
        dados = super().objeto()
        dados.update({
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "id_responsavel": self.id_responsavel
        })

        return dados



