import time
from crud.crud import Crud
from utils.sistema.sistema import limpar_tela
from telas.cadastros.tela_cadastro_doador import TelaCadastrarDoador
from telas.cadastros.tela_cadastro_produtos import TelaCadastrarProdutos
from telas.cadastros.tela_cadastro_Solicitante import TelaCadastrarSolicitante
from utils.exibir_tabela.exibir import exibir_tabela
class TelaVoluntario:
    def __init__(self, usuario):
        self.usuario = usuario
        self.iniciar = True
        self.crud = Crud("jsons/dados_pessoais/usuario.json")
        self.pedidos_aprovados = Crud("jsons/solicitacoes/aprovados.json")
        self.produtos = Crud("jsons/produtos/produtos.json")

    def mostrar(self):

        """
        Mostra a tela de menu do voluntário no terminal.
        """
        while self.iniciar:
            print(f"Voluntário: {self.usuario['nome']}\n\n")
            print("""
            opções:
                1 - cadastrar produto
                2 - cadastrar doador
                3 - cadastrar solicitante
                4 - ver pedidos
                5 - consultar produtos
                0 - sair
            """)

            try:
                opcao = int(input("Digite uma opção: "))

                if opcao == 1:
                    limpar_tela()
                    cadastrar_produto = TelaCadastrarProdutos(self.usuario)
                    cadastrar_produto.mostrar()
                    continue

                elif opcao == 2:
                    limpar_tela()
                    cadastrar_doador = TelaCadastrarDoador(self.usuario)
                    cadastrar_doador.mostrar()
                    continue

                elif opcao == 3:
                    limpar_tela()
                    cadastrar_solicitante = TelaCadastrarSolicitante(self.usuario)
                    cadastrar_solicitante.mostrar()
                    continue

                elif opcao == 4:
                    limpar_tela()
                    self._ver_pedidos()
                    continue

                elif opcao == 5:
                    limpar_tela()
                    self._consultar_produtos()
                    continue

                elif opcao == 0:
                    limpar_tela()
                    print("Saindo...")
                    time.sleep(1.5)
                    limpar_tela()
                    return
            except ValueError:
                limpar_tela()
                continue

    def _ver_pedidos(self):
        """
        Mostra todos os pedidos aprovados no terminal.
        """
        for pedido in self.pedidos_aprovados.listar():
            for produto in pedido["pedido"]:
                exibir_tabela(produto)

        input("\nTecle enter para voltar")
        limpar_tela()
        return

    def _consultar_produtos(self):
        """
        Mostra a tela de consultar produtos no terminal.

        Exibe todos os produtos disponíveis e permite ao usuário digitar o nome do produto desejável.
        Se o produto for encontrado, ele exibe as informações do produto e as quantidades disponíveis.
        Se o produto não for encontrado, ele exibe uma mensagem de erro e volta para a tela inicial.
        """

        escolha = input("Digite o nome do produto desejável: ").title()

        consultar_produto = self.produtos.consultar(escolha)

        if not consultar_produto:
            print("Nenhum Produto encontrado\n\n")
            return

        for item in consultar_produto:
            item["quantidade_disponivel"] = item["quantidade"]
            del item["quantidade"]
            del item["id_doador"]
            del item["id_responsavel"]
            exibir_tabela(item)


        print("\n\n")
        input("Pressione enter para voltar")
        limpar_tela()
        return
