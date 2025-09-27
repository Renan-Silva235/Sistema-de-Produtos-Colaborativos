import time
from utils.sistema.sistema import limpar_tela
from telas.menus.tela_menu_cadastros import TelaMenuCadastro
class TelaAdministrador:

    def __init__(self, usuario):
        self.usuario = usuario
        self.iniciar = True


    def mostrar(self):
        """Esse método exibe tela de administrador no terminal."""

        while self.iniciar:
            print(self.usuario["nome"])

            print("ADMINISTRAÇÃO\n")
            print("""
                Bem vindo a tela de administração, aqui você terá poder total sobre o sistema.
                Abaixo temos funcionalidades básicas
                \n""")

            print("""
                1- Cadastros
                2- Relatórios
                3- Controle de Estoque
                4- Solicitações
                0- Sair
                \n""")

            try:
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    limpar_tela()
                    self.telaMenuCadastro = TelaMenuCadastro(self.usuario)
                    self.telaMenuCadastro.mostrar()
                    continue
                if opcao == 2:
                    print("Relatórios")
                    continue
                if opcao == 3:
                    print("Controle de Estoque")
                    continue
                if opcao == 4:
                    print("Solicitações")
                    continue
                if opcao == 0:
                    limpar_tela()
                    print("Voltando a tela inicial...")
                    time.sleep(2)
                    limpar_tela()
                    return
                else:
                    limpar_tela()
                    print("Opção Inválida")
                    limpar_tela()
                    continue
            except ValueError:
                limpar_tela()
                continue
