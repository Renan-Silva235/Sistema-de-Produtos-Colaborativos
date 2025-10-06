import time
from utils.sistema.sistema import limpar_tela
from telas.menus.tela_menu_cadastros import TelaMenuCadastro
from telas.solicitacoes.tela_pedidos import TelaPedidos
from telas.relatorios.tela_relatorio import TelaRelatorio
from telas.controleEstoque.telaControleEstoque import TelaControleEstoque
from crud.crud import Crud

class TelaAdministrador:

    def __init__(self, usuario):
        self.usuario = usuario
        self.iniciar = True
        self.qtdPedidos = Crud("jsons/solicitacoes/pedidos.json").listar()


    def mostrar(self):
        """Esse método exibe tela de administrador no terminal."""

        while self.iniciar:
            print(self.usuario["nome"])

            print("ADMINISTRAÇÃO\n")
            print("""
                Bem vindo a tela de administração, aqui você terá poder total sobre o sistema.
                Abaixo temos funcionalidades básicas
                \n""")

            print(f"""
                1- Cadastros
                2- Relatórios
                3- Controle de Estoque
                4- Solicitações de pedidos ({len(self.qtdPedidos)})
                0- Sair
                \n""")

            try:
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    limpar_tela()
                    telaMenuCadastro = TelaMenuCadastro(self.usuario)
                    telaMenuCadastro.mostrar()
                    continue
                if opcao == 2:
                    limpar_tela()
                    telaRelatorio = TelaRelatorio()
                    telaRelatorio.mostrar()

                    continue
                if opcao == 3:
                    limpar_tela()
                    telaControleEstoque = TelaControleEstoque()
                    telaControleEstoque.mostrar()
                    continue
                if opcao == 4:
                    limpar_tela()
                    telaPedidos = TelaPedidos(self.usuario)
                    telaPedidos.mostrar()
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
