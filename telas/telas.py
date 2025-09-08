from configs_crud.config_crud import Crud
from validacoes.validacoes import Validacoes
import time
import os

class Telas:
    def __init__(self):
        self.crud = Crud()
        self.validar = Validacoes()

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
                os.system("clear")
                self.tela_login()
                break
            elif opcao == 2:
                # recuperar_senha()
                print("Tela esqueceu senha")
                break
            elif opcao == 3:
                print("Tela solicitar")
                # solicitar_cadastro()
                break
            elif opcao == 0:
                os.system("clear")
                print("Saindo...")
                time.sleep(2)
                os.system("clear")
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

                usuario = input("Digite seu email: ")
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

            if(validar_login):
                print("Login realizado com sucesso")
                break
            else:
                os.system("clear")
                print("Login Inválido")
                time.sleep(2)
                os.system("clear")
                continue



tl = Telas()
tl.tela_inicial()
