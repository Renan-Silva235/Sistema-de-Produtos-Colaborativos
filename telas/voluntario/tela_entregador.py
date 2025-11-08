import json
from crud.crud import Crud
from utils.exibir_tabela.exibir import CriarTabelas
from utils.sistema.sistema import Sistema
from tabulate import tabulate


class TelaEntregador:
    """
    Classe responsável pela tela do entregador.

    Permite que entregadores visualizem pedidos aprovados e registrem
    o status da entrega (finalizada ou cancelada), movendo o pedido para o histórico.
    """

    def __init__(self, usuario):
        """
        Inicializa a tela do entregador.

        :param usuario: Dicionário com os dados do entregador logado
        """
        self.usuario = usuario
        self.iniciar = True
        self.aprovadosJson = "jsons/solicitacoes/aprovados.json"
        self.pedidosAprovados = Crud(self.aprovadosJson)
        self.historico = Crud("jsons/solicitacoes/historico.json")

    def mostrar(self):
        """
        Exibe o menu principal do entregador no terminal.

        Lista todos os pedidos aprovados que estão aguardando entrega e permite
        registrar o status da entrega (finalizada ou cancelada).

        :return: None
        """
        while self.iniciar:

            print("PEDIDOS APROVADOS PARA ENTREGA\n")

            if not self.pedidosAprovados.listar():
                print("Nenhum pedido para entrega.")
                input("\nTecle enter para voltar")
                Sistema.limpar_tela()
                return

            for pedido in self.pedidosAprovados.listar():
                for produto in pedido["pedido"]:
                    produto["codigo_pedido"] = pedido["id"]
                    CriarTabelas.exibir_tabela(produto)


            print("""\n
                1 - Registrar Entrega
                0 - sair
                \n\n""")

            try:
                opcao = int(input("Digite uma das opções acima: "))
                if opcao == 1:
                    Sistema.limpar_tela()
                    self._registrar_entrega()
                    continue
                elif opcao == 0:
                    Sistema.limpar_tela()
                    return
                else:
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue

    def _registrar_entrega(self):
        """
        Registra o status de uma entrega.

        Solicita o código do pedido, permite escolher entre entrega finalizada
        ou cancelada, e move o pedido do arquivo de aprovados para o histórico.

        :return: None
        """

        try:
            pegar_id_pedido = int(input("Digite o código do pedido: "))
        except ValueError:
            print("Código inválido.")
            return

        pedidos = self.pedidosAprovados.listar()

        # procura o pedido pelo ID
        pedido_encontrado = next((p for p in pedidos if p["id"] == pegar_id_pedido), None)
        if not pedido_encontrado:
            print("Pedido não encontrado.")
            return

        print("""
        1 - Entrega finalizada
        2 - Entrega cancelada
        0 - Voltar
        """)

        try:
            opcao = int(input("Digite uma das opções acima: "))
        except ValueError:
            Sistema.limpar_tela()
            return

        if opcao == 0:
            Sistema.limpar_tela()
            return

        if opcao not in [1, 2]:
            Sistema.limpar_tela()
            return

        # define o status
        status_entrega = "finalizado" if opcao == 1 else "cancelado"

        # adiciona informações extras no pedido
        pedido_encontrado["status_entrega"] = status_entrega
        pedido_encontrado["id_entregador"] = self.usuario["id"]
        pedido_encontrado["codigo_pedido"] = pedido_encontrado["id"]
        del pedido_encontrado["id"]

        # salva no histórico
        self.historico.cadastrar(pedido_encontrado)

        pedido_encontrado["id"] = pegar_id_pedido
        # remove o pedido do aprovados.json
        pedidos = [p for p in pedidos if p["id"] != pegar_id_pedido]

        # sobrescreve o arquivo aprovados.json
        with open(self.aprovadosJson, "w", encoding="utf-8") as f:
            json.dump(pedidos, f, ensure_ascii=False, indent=4)

        Sistema.limpar_tela()
        return




