import time
from usuarios.login import Login
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.sistema.sistema import limpar_tela
from telas.admin.tela_administrador import TelaAdministrador
from telas.solicitantes.tela_solicitantes import TelaSolicitantes


class TelaLogin:

    def __init__(self):
        self.validar = ValidacoesUsuario()
        self.iniciar = True
        self.niveis = ["Administrador", "Voluntário", "Solicitante"]


    def mostrar(self):
        """Esse método exibe a tela de login no terminal."""


        while self.iniciar:
            print("LOGIN")
            try:
                try:
                    nivel = int(input(f"Informe a opção do seu nível: (1- {self.niveis[0]}, 2- {self.niveis[1]}, 3- {self.niveis[2]}, 0- sair): "))
                    if nivel not in [1,2,3,0]:
                        limpar_tela()
                        continue

                    elif nivel == 0:
                        limpar_tela()
                        print("Saindo...")
                        time.sleep(1.5)
                        limpar_tela()
                        return

                except ValueError:
                    limpar_tela()
                    continue

                email = input("Digite seu email: ").lower()
                ValidacoesUsuario.validar_email(email)

                senha = input("Digite sua senha: ")
                ValidacoesUsuario.validar_senha(senha)

            except ValueError as erro:
                limpar_tela()
                print(erro)
                continue



            if nivel == 1:
                login = Login("jsons/dados_pessoais/usuario.json")
                autenticar = login.autenticar(email=email, senha=senha)

                if autenticar:
                    limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    limpar_tela()
                    telaAdministrador = TelaAdministrador(autenticar)
                    telaAdministrador.mostrar()
                    continue
                else:
                    limpar_tela()
                    print("Login Inválido")
                    time.sleep(1)
                    limpar_tela()
                    continue

            elif nivel == 3:
                login = Login("jsons/dados_pessoais/solicitantes.json")
                autenticar = login.autenticar(email=email, senha=senha)

                if autenticar:
                    limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    limpar_tela()
                    telaSolicitantes = TelaSolicitantes(autenticar)
                    telaSolicitantes.mostrar()
                    continue
                else:
                    limpar_tela()
                    print("Login Inválido")
                    time.sleep(1)
                    limpar_tela()
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

            # else:
            #     limpar_tela()
            #     print("Login Inválido")
            #     time.sleep(1)
            #     limpar_tela()
            #     continue
            # if nivel == 1:
                # self.gerenciador.mudar_tela("TelaAdministrador")
                # return
            # elif nivel == 2:
                # print("")
                # self.tela_voluntario(TelaVoluntario)
            # elif nivel == 3:
            #     print("")
                # self.gerenciador.mudar_tela(TelaSolicitante)
