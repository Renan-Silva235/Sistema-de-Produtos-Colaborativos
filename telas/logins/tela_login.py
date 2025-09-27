import time
from usuarios.gerenciador import Gerenciador
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.sistema.sistema import limpar_tela
from telas.admin.tela_administrador import TelaAdministrador


class TelaLogin:

    def __init__(self):
        self.validar = ValidacoesUsuario()
        self.jsonUsuario = "jsons/dados_pessoais/usuario.json"
        self.gerenciador = Gerenciador(self.jsonUsuario)
        self.iniciar = True


    def mostrar(self):
        """Esse método exibe a tela de login no terminal."""


        while self.iniciar:
            print("LOGIN")
            try:
                email = input("Digite seu email: ").lower()
                ValidacoesUsuario.validar_email(email)

                senha = input("Digite sua senha: ")
                ValidacoesUsuario.validar_senha(senha)

            except ValueError as erro:
                limpar_tela()
                print(erro)
                continue


            login = self.gerenciador.login(email=email, senha=senha)

            if login:
                if login["nivel"] == "Administrador":
                    limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    limpar_tela()
                    self.telaAdministrador = TelaAdministrador(login)
                    self.telaAdministrador.mostrar()
                    continue

            # elif login["nivel"] == niveis[1]:

            #     limpar_tela()
            #     print("Login realizado com sucesso")
            #     time.sleep(1.5)
            #     limpar_tela()
            #     self.telaAdministrador.mostrar(login)
            # if login["nivel"] == niveis[0]:
            #     limpar_tela()
            #     print("Login realizado com sucesso")
            #     time.sleep(1.5)
            #     limpar_tela()
            #     self.telaAdministrador.mostrar(login)

            else:
                limpar_tela()
                print("Login Inválido")
                time.sleep(1)
                limpar_tela()
                continue
            # if nivel == 1:
                # self.gerenciador.mudar_tela("TelaAdministrador")
                # return
            # elif nivel == 2:
                # print("")
                # self.tela_voluntario(TelaVoluntario)
            # elif nivel == 3:
            #     print("")
                # self.gerenciador.mudar_tela(TelaSolicitante)
