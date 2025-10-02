import time
from utils.sistema.sistema import limpar_tela
from telas.logins.tela_login import TelaLogin
from telas.recuperar_senha.tela_recuperar_senha import TelaRecuperarSenha
class TelaInicial:

    def __init__(self):
        self.iniciar = True
        self.telaLogin = TelaLogin()
        self.telaRecuperarSenha = TelaRecuperarSenha()

    def mostrar(self):
        """Esse método exibe tela Inicial no terminal."""

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
                    limpar_tela()
                    self.telaLogin.mostrar()
                    continue
                elif opcao == 2:
                    limpar_tela()
                    self.telaRecuperarSenha.mostrar()
                    continue
                elif opcao == 0:
                    limpar_tela()
                    print("Saindo...")
                    time.sleep(1.5)
                    limpar_tela()
                    return
                else:
                    print("Opção inválida, Tente Novamente: ")
                    time.sleep(1)
                    limpar_tela()
                    continue

            except ValueError:
                limpar_tela()
                continue


