import time
import json
from utils.sistema.sistema import limpar_tela
from validacoes.validacao import Validacoes

class TelaRecuperarSenha:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def mostrar(self):
        """Esse método exibe a tela de recuperação de senha no terminal."""

        print("Informe os dados abaixo para recuperar a sua senha: ")

        while True:
            try:
                opcao = int(input("digite (1) Informar os dados / (2) cancelar: "))

                if opcao not in [1, 2]:
                    print("Opção inválida. Digite (1 ou 2)")
                    continue
                break
            except ValueError:
                print("Digite apenas números (1 ou 2)")
                continue

        if opcao == 1:
            informar_nivel = int(input("Informe seu nível de acesso: (1) Administrador | (2) Voluntário | (3) Solicitante: "))
            informar_cpf = input("Digite o seu cpf: ")
            informar_email = input("Digite seu e-mail: ").lower()

            nova_senha = self.gerar_nova_senha(informar_nivel, informar_cpf, informar_email)
            if not nova_senha:
                time.sleep(2)
                limpar_tela()
                self.gerenciador.mudar_tela("TelaRecuperarSenha")

            else:
                time.sleep(2)
                limpar_tela()
                print("Voltando para a tela inicial...")
                time.sleep(2)
                limpar_tela()
                self.gerenciador.mudar_tela("TelaInicial")

        if opcao == 2:
            limpar_tela()
            print("Voltando para a Tela Inicial...")
            time.sleep(2)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaInicial")


    def _gerar_nova_senha(self,nivel, cpf, email):
        """Esse método abre um campo para o usuário digitar a nova senha."""

        usuario_encontrado = None

        if nivel == 1:
            arquivo = "json/dados_funcionarios.json"
            nivel_usuario = "Administrador"
        elif nivel == 2:
            arquivo = "json/dados_funcionarios.json"
            nivel_usuario = "Voluntário"
        elif nivel == 3:
            arquivo = "json/dados_solicitantes.json"
            nivel_usuario = "Solicitante"
        else:
            print("Nível inválido.")
            return False

        if not Validacoes.validar_cpf(cpf):
            print("CPF inválido.")
            return False

        if not Validacoes.validar_email(email):
            print("E-mail inválido.")
            return False

        with open(arquivo, "r", encoding="utf-8") as arq:
            usuarios = json.load(arq)

        email = email.strip().lower()
        cpf = cpf.strip()

        for i, user in enumerate(usuarios):
            if user.get("nivel") == nivel_usuario and user.get("cpf") == cpf and user.get("emailCorporativo") == email:
                usuario_encontrado = user
                break

        if not usuario_encontrado:
            print("Usuário não encontrado")
            return False

        while True:
            nova_senha = input("Digite sua nova senha (4 dígitos numéricos): ")
            if len(nova_senha) != 4 or not nova_senha.isdigit():
                limpar_tela()
                print("Formato inválido. A senha precisa ter exatamente 4 dígitos numéricos.")
                time.sleep(2)
                limpar_tela()
                continue
            break

        while True:
            redigitar = input("Digite novamente a nova senha: ")
            if redigitar != nova_senha:
                print("Senhas não coincidem, tente novamente")
                time.sleep(2)
                continue
            break

        usuario_encontrado["senha"] = nova_senha

        with open(arquivo, "w", encoding="utf-8") as arq:
            json.dump(usuarios, arq, indent=4, ensure_ascii=False)

        print("Senha alterada com sucesso!")
        return True
