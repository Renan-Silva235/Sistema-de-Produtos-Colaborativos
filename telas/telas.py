import time
from utils.sistema import limpar_tela
from funcoes_auxiliares_python.funcoes_auxiliares import gerar_nova_senha
from configs_crud.config_crud import Crud
from validacoes.validacoes import Validacoes

class Telas:
    def __init__(self):
        self.crud = Crud()
        self.validar = Validacoes()
        self.arquivo_funcionarios_json = "json/dados_funcionarios.json"
        self.arquivo_solicitantes_json = "json/dados_solicitantes.json"

    def tela_inicial(self):
        print("TELA INICIAL:")

        print("""
                1 - Login
                2 - Esqueceu Senha
                3 - Solicitar Cadastro como solicitante
                0 - Sair
        """)
        opcao = True

        while opcao:

            opcao = int(input("Digite uma das opções acima: "))
            if opcao == 1:
                limpar_tela()
                self.tela_login()
                break
            elif opcao == 2:
                limpar_tela()
                self.tela_recuperar_senha()
                break
            elif opcao == 3:
                print("Tela solicitar")
                # solicitar_cadastro()
                break
            elif opcao == 0:
                limpar_tela()
                print("Saindo...")
                time.sleep(2)
                limpar_tela()
                break
            else:
                print("Opção inválida, Tente Novamente: ")


    def tela_login(self):

        print("LOGIN")

        while True:

            while True:
                try:
                    nivel = int(input("Qual seu nível? ( 1- Administrador/ 2- Voluntário/ 3- Solicitante): "))
                    if nivel not in [1, 2, 3]:
                        print("Opção inválida. Digite 1, 2 ou 3.")
                        continue
                    break
                except ValueError:
                    print("Digite apenas números (1, 2 ou 3).")
                    continue

            while True:

                usuario = input("Digite seu email: ").lower()
                if usuario == "":
                    print("Login Incorreto, campo usuário vazio")
                    continue
                break


            while True:
                senha = input("Digite sua senha: ")
                if senha == "":
                    print("Senha Incorreta, campo senha vazio")
                    continue
                elif not senha.isdigit():
                    print("Senha incorreta, senha precisa ser numérica")
                    continue
                elif len(senha) < 4 or len(senha) > 4:
                    print("Senha Incorreta, senha precisa ter 4 números")
                    continue
                break


            validar_login = self.validar.validar_login(nivel, usuario, senha)

            if validar_login:
                limpar_tela()
                print("Login realizado com sucesso")
                time.sleep(2)
                limpar_tela()
                break

            else:
                limpar_tela()
                print("Login Inválido")
                time.sleep(2)
                limpar_tela()
                continue

        if nivel == 1:
            self.tela_administrador()
        elif nivel == 2:
            self.tela_voluntario()
        elif nivel == 3:
            self.tela_solicitante()

    def tela_recuperar_senha(self):
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

            nova_senha = gerar_nova_senha(informar_nivel, informar_cpf, informar_email)
            if not nova_senha:
                time.sleep(2)
                limpar_tela()
                self.tela_recuperar_senha()

            else:
                time.sleep(2)
                limpar_tela()
                print("Voltando para a tela inicial...")
                time.sleep(2)
                limpar_tela()
                self.tela_inicial()



        if opcao == 2:
            limpar_tela()
            print("Voltando para a Tela Inicial...")
            time.sleep(2)
            limpar_tela()
            self.tela_inicial()


    def tela_administrador(self):
        print("BEM VINDO A TELA DE ADMINISTRADOR")


tl = Telas()
tl.tela_inicial()
