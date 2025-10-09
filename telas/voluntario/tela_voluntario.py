import time
from crud.crud import Crud
from utils.sistema.sistema import Sistema
from telas.cadastros.tela_cadastro_doador import TelaCadastrarDoador
from telas.cadastros.tela_cadastro_produtos import TelaCadastrarProdutos
from telas.cadastros.tela_cadastro_Solicitante import TelaCadastrarSolicitante
from telas.controleEstoque.telaControleEstoque import TelaControleEstoque
from utils.exibir_tabela.exibir import CriarTabelas
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
                5 - controle de estoque
                0 - sair
            """)

            try:
                opcao = int(input("Digite uma opção: "))

                if opcao == 1:
                    Sistema.limpar_tela()
                    cadastrar_produto = TelaCadastrarProdutos(self.usuario)
                    cadastrar_produto.mostrar()
                    continue

                elif opcao == 2:
                    Sistema.limpar_tela()
                    cadastrar_doador = TelaCadastrarDoador(self.usuario)
                    cadastrar_doador.mostrar()
                    continue

                elif opcao == 3:
                    Sistema.limpar_tela()
                    cadastrar_solicitante = TelaCadastrarSolicitante(self.usuario)
                    cadastrar_solicitante.mostrar()
                    continue

                elif opcao == 4:
                    Sistema.limpar_tela()
                    self._ver_pedidos()
                    continue

                elif opcao == 5:
                    Sistema.limpar_tela()
                    controle_estoque = TelaControleEstoque()
                    controle_estoque.mostrar()
                    continue

                elif opcao == 0:
                    Sistema.limpar_tela()
                    print("Saindo...")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return
            except ValueError:
                Sistema.limpar_tela()
                continue

    def _ver_pedidos(self):
        """
        Mostra todos os pedidos aprovados no terminal.
        """
        for pedido in self.pedidos_aprovados.listar():
            for produto in pedido["pedido"]:
                CriarTabelas.exibir_tabela(produto)

        input("\nTecle enter para voltar")
        Sistema.limpar_tela()
        return

