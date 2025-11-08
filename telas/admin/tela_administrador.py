import time
from utils.sistema.sistema import Sistema
from telas.menus.tela_menu_cadastros import TelaMenuCadastro
from telas.solicitacoes.tela_pedidos import TelaPedidos
from telas.relatorios.tela_relatorio import TelaRelatorio
from telas.controleEstoque.telaControleEstoque import TelaControleEstoque
from crud.crud import Crud


class TelaAdministrador:
    """
    Classe responsável pela tela principal de administração do sistema.

    Fornece acesso às funcionalidades administrativas: cadastros, relatórios,
    controle de estoque e gerenciamento de solicitações de pedidos.
    """

    def __init__(self, usuario):
        """
        Inicializa a tela de administrador.

        :param usuario: Dicionário com os dados do usuário administrador logado
        """
        self.usuario = usuario
        self.iniciar = True
        self.qtdPedidos = Crud("jsons/solicitacoes/pedidos.json").listar()

    def mostrar(self):
        """
        Exibe a tela de administração no terminal.

        Apresenta um menu com as opções disponíveis para o administrador:
        - Cadastros (doadores, solicitantes, voluntários, produtos)
        - Relatórios do sistema
        - Controle de estoque
        - Solicitações de pedidos (com contador)
        - Sair do sistema

        :return: None
        """

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
                    Sistema.limpar_tela()
                    telaMenuCadastro = TelaMenuCadastro(self.usuario)
                    telaMenuCadastro.mostrar()
                    continue
                if opcao == 2:
                    Sistema.limpar_tela()
                    telaRelatorio = TelaRelatorio()
                    telaRelatorio.mostrar()

                    continue
                if opcao == 3:
                    Sistema.limpar_tela()
                    telaControleEstoque = TelaControleEstoque()
                    telaControleEstoque.mostrar()
                    continue
                if opcao == 4:
                    Sistema.limpar_tela()
                    telaPedidos = TelaPedidos(self.usuario)
                    telaPedidos.mostrar()
                    continue
                if opcao == 0:
                    Sistema.limpar_tela()
                    print("Voltando a tela inicial...")
                    time.sleep(2)
                    Sistema.limpar_tela()
                    return
                else:
                    Sistema.limpar_tela()
                    print("Opção Inválida")
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue
