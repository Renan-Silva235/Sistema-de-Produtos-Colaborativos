import time
from utils.sistema import limpar_tela

class TelaInicial:

    def __init__(self, gerenciador):
        self.gerenciador = gerenciador


    def mostrar(self):
        """Esse método exibe tela Inicial no terminal."""

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
                self.gerenciador.mudar_tela("TelaLogin")
                opcao = False
            elif opcao == 2:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaRecuperarSenha")
                opcao = False
            elif opcao == 3:
                print("Tela solicitar")
                # solicitar_cadastro()
                opcao = False
            elif opcao == 0:
                limpar_tela()
                print("Saindo...")
                time.sleep(2)
                limpar_tela()
                opcao = False
            else:
                print("Opção inválida, Tente Novamente: ")
