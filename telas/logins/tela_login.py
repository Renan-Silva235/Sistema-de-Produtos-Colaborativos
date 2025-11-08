import time
from usuarios.login import Login
from usuarios.usuario import PerfilUsuario
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.sistema.sistema import Sistema
from telas.admin.tela_administrador import TelaAdministrador
from telas.solicitantes.tela_solicitantes import TelaSolicitantes
from telas.voluntario.tela_voluntario import TelaVoluntario
from telas.voluntario.tela_entregador import TelaEntregador


class TelaLogin:
    """
    Classe responsável pela tela de login do sistema.

    Permite autenticação de funcionários (Administrador, Atendente, Entregador)
    e clientes (solicitantes), direcionando para a tela apropriada após o login.
    """

    def __init__(self):
        """
        Inicializa a tela de login.
        """
        self.perfil = PerfilUsuario()
        self.validar = ValidacoesUsuario()
        self.iniciar = True
        self.niveis = ["Funcionário", "Cliente"]

    def mostrar(self):
        """
        Exibe a tela de login no terminal.

        Solicita o nível do usuário (Funcionário ou Cliente), email e senha,
        valida as credenciais e direciona para a tela apropriada conforme o cargo.

        :return: None
        """


        while self.iniciar:
            print("LOGIN")
            try:
                try:
                    nivel = int(input(f"Informe a opção do seu nível: (1- {self.niveis[0]}, 2- {self.niveis[1]},  0- sair): "))
                    if nivel not in [1,2,0]:
                        Sistema.limpar_tela()
                        continue

                    elif nivel == 0:
                        Sistema.limpar_tela()
                        print("Saindo...")
                        time.sleep(1.5)
                        Sistema.limpar_tela()
                        return

                except ValueError:
                    Sistema.limpar_tela()
                    continue

                email = input("Digite seu email: ").lower()
                ValidacoesUsuario.validar_email(email)

                senha = input("Digite sua senha: ")
                ValidacoesUsuario.validar_senha(senha)

            except ValueError as erro:
                Sistema.limpar_tela()
                print(erro)
                continue



            if nivel == 1:
                login = Login("jsons/dados_pessoais/usuario.json")
                autenticar = login.autenticar(email=email, senha=senha)

                if autenticar["cargo"] == "Administrador":
                    Sistema.limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    telaAdministrador = TelaAdministrador(autenticar)
                    telaAdministrador.mostrar()
                    continue
                elif autenticar["cargo"] == "Atendente":
                    Sistema.limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    telaVoluntario = TelaVoluntario(autenticar)
                    telaVoluntario.mostrar()
                    continue

                elif autenticar["cargo"] == "Entregador":
                    Sistema.limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    telaEntregador = TelaEntregador(autenticar)
                    telaEntregador.mostrar()
                    continue

                else:
                    Sistema.limpar_tela()
                    print("Login Inválido")
                    time.sleep(1)
                    Sistema.limpar_tela()
                    continue

            elif nivel == 2:
                login = Login("jsons/dados_pessoais/solicitantes.json")
                autenticar = login.autenticar(email=email, senha=senha)

                if autenticar:
                    Sistema.limpar_tela()
                    print("Login realizado com sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    telaSolicitante = TelaSolicitantes(autenticar)
                    telaSolicitante.mostrar()
                    continue
                else:
                    Sistema.limpar_tela()
                    print("Login Inválido")
                    time.sleep(1)
                    Sistema.limpar_tela()
                    continue

