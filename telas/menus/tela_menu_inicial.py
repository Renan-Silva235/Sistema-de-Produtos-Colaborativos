import time
from utils.sistema.sistema import Sistema
from telas.logins.tela_login import TelaLogin
from telas.recuperar_senha.tela_recuperar_senha import TelaRecuperarSenha


class TelaInicial:
    """
    Classe responsável pela tela inicial do sistema.

    Primeira tela exibida ao iniciar o programa, oferecendo opções de login,
    recuperação de senha ou saída do sistema.
    """

    def __init__(self):
        """
        Inicializa a tela inicial.
        """
        self.iniciar = True
        self.telaLogin = TelaLogin()
        self.telaRecuperarSenha = TelaRecuperarSenha()

    def mostrar(self):
        """
        Exibe a tela inicial no terminal.

        Apresenta um menu com as opções: Login, Esqueceu Senha e Sair.
        Direciona para a tela apropriada conforme a escolha do usuário.

        :return: None
        """

        while self.iniciar:
            print("TELA INICIAL:")

            print("""
                    1 - Login
                    2 - Esqueceu Senha
                    0 - Sair
            """)


            try:
                opcao = int(input("Digite uma das opções acima: "))
                if opcao == 1:
                    Sistema.limpar_tela()
                    self.telaLogin.mostrar()
                    continue
                elif opcao == 2:
                    Sistema.limpar_tela()
                    self.telaRecuperarSenha.mostrar()
                    continue
                elif opcao == 0:
                    Sistema.limpar_tela()
                    print("Saindo...")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return
                else:
                    print("Opção inválida, Tente Novamente: ")
                    time.sleep(1)
                    Sistema.limpar_tela()
                    continue

            except ValueError:
                Sistema.limpar_tela()
                continue


