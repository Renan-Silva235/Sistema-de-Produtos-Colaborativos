import json

class Validacoes:

    def validar_login(self, nivel, usuario, senha):
        arquivo = None
        nivel_usuario = None
        logado = False

        if nivel == 1:
            arquivo = "json/dados_funcionarios.json"
            nivel_usuario = "Administrador"
        elif nivel == 2:
            arquivo = "json/dados_funcionarios.json"
            nivel_usuario = "Voluntário"
        else:
            arquivo = "json/dados_solicitantes.json"
            nivel_usuario = "Solicitante"

        with open(arquivo, "r", encoding="utf-8") as arq:
            usuarios = json.load(arq)

        for user in usuarios:
            if nivel_usuario == "Solicitante":
                if user.get("email") == usuario and user.get("senha") == senha:
                    logado = True
                    return logado
            elif user.get("nivel") == nivel_usuario and user.get("emailCorporativo") == usuario and user.get("senha") == senha:
                logado = True
                return logado


        return logado



