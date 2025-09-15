import time
from validacoes.validacao import Validacoes
from utils.sistema.sistema import limpar_tela


class TelaLogin:

    def __init__(self, gerenciador):
        self.validar = Validacoes()
        self.gerenciador = gerenciador


    def mostrar(self):
        """Esse método exibe a tela de login no terminal."""

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
                email = input("Digite seu email: ").lower()
                if not Validacoes.validar_email(email):
                    print("E-mail Inválido")
                    continue
                break



            while True:
                senha = input("Digite sua senha: ")
                if not Validacoes.validar_senha(senha):
                    print("Senha inválida, A senha precisa ter 4 digitos e ser numérica")
                    continue
                break

            if self.validar.validar_login(nivel, email, senha):
                limpar_tela()
                print("Login realizado com sucesso")
                limpar_tela()
                break
            else:
                limpar_tela()
                print("Login Inválido")
                time.sleep(1)
                limpar_tela()
                continue

        if nivel == 1:
            self.gerenciador.mudar_tela("TelaAdministrador")
            return
        elif nivel == 2:
            print("")
            # self.tela_voluntario(TelaVoluntario)
        elif nivel == 3:
            print("")
            # self.gerenciador.mudar_tela(TelaSolicitante)
