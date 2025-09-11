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

        opcao = int(input("Digite uma das opções acima: "))
        if opcao == 1:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaLogin")
            return
        elif opcao == 2:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaRecuperarSenha")
            return
        elif opcao == 3:
            print("Tela solicitar")
            return
            # solicitar_cadastro()
        elif opcao == 0:
            limpar_tela()
            print("Saindo...")
            time.sleep(2)
            limpar_tela()
            return
        else:
            print("Opção inválida, Tente Novamente: ")
            time.sleep(1)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaInicial")
            return
