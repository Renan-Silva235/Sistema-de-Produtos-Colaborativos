import time
from utils.sistema import limpar_tela

class TelaAdministrador:

    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def mostrar(self):
        """Esse método exibe tela de administrador no terminal."""

        print("ADMINISTRAÇÃO")
        print("""
              Bem vindo a tela de administração, aqui você terá poder total sobre o sistema.
              Abaixo temos funcionalidades básicas
              """)

        print("""
            1- Cadastros
            2- Relatórios
            3- Controle de Estoque
            4- Solicitações
            0- Sair
            """)

        while True:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaMenuCadastro")
                break
            if opcao == 2:
                print("Relatórios")
                break
            if opcao == 3:
                print("Controle de Estoque")
                break
            if opcao == 4:
                print("Solicitações")
                break
            if opcao == 0:
                limpar_tela()
                print("Voltando a tela inicial...")
                time.sleep(2)
                limpar_tela()
                self.gerenciador.mudar_tela("TelaInicial")
                limpar_tela()
                break
            else:
                limpar_tela()
                print("Opção Inválida")
                limpar_tela()
                continue
