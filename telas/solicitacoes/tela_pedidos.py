import json
from utils.sistema.sistema import limpar_tela
from crud.crud import Crud
from utils.exibir_tabela.exibir import exibir_tabela
class TelaPedidos:
    def __init__(self, usuario):
        """
        Inicializa a tela de pedidos solicitados.

        Recebe o usuário e seus respectivos arquivos json que serão manipulados.

        self.usuario: o usuário que está acessando a tela
        self.json_estoque: o caminho do arquivo json que contém os produtos em estoque
        self.json_aprovados: o caminho do arquivo json que contém os produtos aprovados
        self.json_pedidos: o caminho do arquivo json que contém os produtos pedidos
        self.json_reprovados: o caminho do arquivo json que contém os produtos reprovados
        self.pedidos: o gerenciador do arquivo json que contém os produtos pedidos
        self.aprovados: o gerenciador do arquivo json que contém os produtos aprovados
        self.reprovado: o gerenciador do arquivo json que contém os produtos reprovados
        self.estoque: o gerenciador do arquivo json que contém os produtos em estoque
        self.iniciar: um booleano que indica se a tela deve ser exibida novamente
        self.status: uma lista que contém os status possíveis para um produto (aprovado ou reprovado)
        """
        self.usuario = usuario
        self.json_estoque = "jsons/produtos/produtos.json"
        self.json_aprovados = "jsons/solicitacoes/aprovados.json"
        self.json_pedidos = "jsons/solicitacoes/pedidos.json"
        self.json_reprovados = "jsons/solicitacoes/reprovados.json"
        self.pedidos = Crud(self.json_pedidos)
        self.aprovados = Crud(self.json_aprovados)
        self.reprovado = Crud(self.json_reprovados)
        self.estoque = Crud(self.json_estoque)
        self.iniciar = True
        self.status = ["Aprovado", "Reprovado"]

    def mostrar(self):
        """
        Mostra a tela de pedidos solicitados no terminal.

        Exibe todos os produtos solicitados e permite ao usuário aprovar ou reprovar o pedido.
        Se o usuário aprovar o pedido, o produto é adicionado à lista de aprovados e sua quantidade é atualizada no estoque.
        Se o usuário reprovar o pedido, o produto é removido da lista de pedidos.
        """
        while self.iniciar:
            print("PEDIDOS SOLICITADOS: \n\n")

            for pedido in self.pedidos.listar():
                for produto in pedido["pedido"]:
                    exibir_tabela(produto)

            pegar_id = int(input("\nDigite o número do Id correspondente ou '0' para voltar: "))

            if pegar_id == 0:
                limpar_tela()
                return

            for pedido in self.pedidos.listar():
                for produto in pedido["pedido"]:
                    if pegar_id == produto["id"]:
                        status = int(input("""
                                           Digite a opção com a ação desejada:
                                           1- Aprovado
                                           2- reprovado
                                           0- voltar

                                           opção: """))

                        if status == 1:

                            produto["id_responsavel"] = self.usuario["id"]
                            produto["status"] = self.status[0]
                            del pedido["id"]
                            self.aprovados.cadastrar(pedido)

                            for itens in self.estoque.listar():
                                if pegar_id == itens["id"]:
                                    estoque_atualizado = itens["quantidade"] - produto["quantidade_pedida"]
                                    # alterar = Alteracoes()
                                    self.estoque.atualizar("id", itens["quantidade"], estoque_atualizado)
                                    # alterar.alterar_estoque(self.json_estoque, pegar_id, estoque_atualizado)

                            pedidos = [p for p in self.pedidos.listar() if p.get("id") != pegar_id]

                            with open(self.json_pedidos, "w", encoding="utf-8") as f:
                                json.dump(pedidos, f, indent=4, ensure_ascii=False)

                            break

                        elif status == 2:
                            produto["id_responsavel"] = self.usuario["id"]
                            produto["status"] = self.status[1]
                            self.reprovado.cadastrar(pedido)

                            pedidos = [p for p in self.pedidos.listar() if p.get("id") != pegar_id]

                            with open(self.json_reprovados, "w", encoding="utf-8") as f:
                                json.dump(pedidos, f, indent=4, ensure_ascii=False)

                            continue
                        elif status == 0:
                            limpar_tela()
                            break




# tela = TelaPedidos("Renan")
# tela.mostrar()
