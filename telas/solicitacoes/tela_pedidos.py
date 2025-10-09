import json
import time
from utils.exibir_tabela.exibir import CriarTabelas
from utils.sistema.sistema import Sistema
from crud.crud import Crud

class TelaPedidos:
    def __init__(self, usuario):
        """
        Inicializa a tela de pedidos.
        """
        self.usuario = usuario
        self.aprovados = Crud("jsons/solicitacoes/aprovados.json")
        self.reprovados = Crud("jsons/solicitacoes/reprovados.json")
        self.pedidos = Crud("jsons/solicitacoes/pedidos.json")
        self.produtos = Crud("jsons/produtos/produtos.json")


    def mostrar(self):
        """
        Mostra a tela de pedidos solicitados no terminal.

        Exibe todos os pedidos solicitados e permite ao usuário digitar o identificador do pedido desejado.
        Se o pedido for encontrado, ele exibe as informações do pedido e as quantidades disponíveis.
        Se o pedido não for encontrado, ele exibe uma mensagem de erro e volta para a tela inicial.

        Permite ao usuário aprovar ou reprovar o pedido.
        """
        while True:
            Sistema.limpar_tela()

            if not self.pedidos.listar():
                print("Não há pedidos no momento.")
                input("Tecle enter para voltar")
                Sistema.limpar_tela()
                return


            print("PEDIDOS SOLICITADOS: \n\n")

            for pedido in self.pedidos.listar():
                for produto in pedido["pedido"]:
                    CriarTabelas.exibir_tabela(produto)

            try:
                pegar_id = int(input("\nDigite o número do Id correspondente ou '0' para voltar: "))

                if pegar_id == 0:
                    Sistema.limpar_tela()
                    print("Voltando...")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return
            except ValueError:
                Sistema.limpar_tela()
                continue

            encontrado = False
            for pedido in self.pedidos.listar():
                for produto in pedido["pedido"]:
                    if pegar_id == produto["id"]:
                        encontrado = True
                        break
                if encontrado:
                    break

            if not encontrado:
                print("Pedido não encontrado.")
                continue

            status = input("""
                                Digite a opção com a ação desejada:
                                1- Aprovado
                                2- Reprovado
                                0- Voltar

                                opção: """)

            if status == "1":
                self._aprovar_pedido(pegar_id)
            elif status == "2":
                self._reprovar_pedido(pegar_id)
            elif status == "0":
                return

    def _aprovar_pedido(self, id):
        """
        Aprova um pedido de acordo com o id.
        """
        pedidos = self.pedidos.listar()

        for pedido in pedidos:
            for produto in pedido["pedido"]:
                for item in self.produtos.listar():
                    if produto["id"] == item["id"]:
                        estoque_atualizado = item["quantidade"] - produto["quantidade_pedida"]
                        self.produtos.atualizar(item["id"], "quantidade", estoque_atualizado)


                if produto["id"] == id:
                    produto["responsavel"] = self.usuario["nome"]
                    produto["status"] = "Aprovado"
                    pedido_copia = pedido.copy()
                    del pedido_copia["id"]
                    self.aprovados.cadastrar(pedido_copia)
                    pedido["pedido"].remove(produto)

                    if not pedido["pedido"]:
                        pedidos.remove(pedido)

                    with open(self.pedidos.json, "w", encoding="utf-8") as f:
                        json.dump(pedidos, f, ensure_ascii=False, indent=4)

                    return

    def _reprovar_pedido(self, id):
        """
        Reprova um pedido de acordo com o id.
        """
        pedidos = self.pedidos.listar()
        for pedido in pedidos:
            for produto in pedido["pedido"]:
                if produto["id"] == id:
                    produto["responsavel"] = self.usuario["nome"]
                    produto["status"] = "Reprovado"
                    pedido_copia = pedido.copy()
                    del pedido_copia["id"]
                    self.reprovados.cadastrar(pedido_copia)
                    pedido["pedido"].remove(produto)

                    if not pedido["pedido"]:
                        pedidos.remove(pedido)

                    with open(self.pedidos.json, "w", encoding="utf-8") as f:
                        json.dump(pedidos, f, ensure_ascii=False, indent=4)

                    return







