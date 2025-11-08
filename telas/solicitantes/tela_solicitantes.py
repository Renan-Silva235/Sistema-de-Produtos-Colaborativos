import time
from crud.crud import Crud
from utils.sistema.sistema import Sistema
from utils.exibir_tabela.exibir import CriarTabelas


class TelaSolicitantes:
    """
    Classe responsável pela tela do solicitante (cliente).

    Permite que solicitantes consultem produtos disponíveis, façam pedidos
    e visualizem o status de seus pedidos (em análise, aprovados ou reprovados).
    """

    def __init__(self, usuario):
        """
        Inicializa a tela do solicitante.

        :param usuario: Dicionário com os dados do solicitante logado
        """
        self.usuario = usuario
        self.produtos = Crud("jsons/produtos/produtos.json")
        self.pedidos = Crud("jsons/solicitacoes/pedidos.json")
        self.produtos_aprovados = Crud("jsons/solicitacoes/aprovados.json")
        self.produtos_reprovados = Crud("jsons/solicitacoes/reprovados.json")
        self.iniciar = True
        self.categorias = ["Vestuário", "Medicamentos", "Alimentícios"]

    def mostrar(self):
        """
        Exibe o menu principal do solicitante no terminal.

        Apresenta as opções disponíveis:
        - Consultar Produto
        - Fazer pedido
        - Ver status dos pedidos
        - Voltar

        :return: None
        """

        print(f"Solicitante: {self.usuario["nome"]}\n\n")
        while self.iniciar:
            print("""
                Seja Bem-Vindo(a) ao nosso sistema de Doações, aqui você poderá consultar alguns produtos que estão disponíveis
                para doação e fazer pedidos. Seus pedidos serão avaliados pela nossa equipe de Administração, caso seja aprovado
                ou não você será notificado(a) pela aba pedidos. Em caso de aprovação, seu pedido será entregue no seu endereço
                cadastrado.\n\n""")

            print("1 - Consultar Produto")
            print("2 - Fazer pedido")
            print("3 - pedidos")
            print("0 - voltar\n")

            try:
                opcao = int(input("Digite uma das opções acima: "))

                if opcao == 1:
                    Sistema.limpar_tela()
                    self._consultar_produtos()
                    continue

                elif opcao == 2:
                    Sistema.limpar_tela()
                    self._fazer_pedido()
                    continue

                elif opcao == 3:
                    Sistema.limpar_tela()
                    self._status_pedidos()
                    continue

                elif opcao == 0:
                    if opcao == 0:
                        Sistema.limpar_tela()
                        print("Voltando...")
                        time.sleep(1.2)
                        Sistema.limpar_tela()
                        return
                else:
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue

    def _consultar_produtos(self):
        """
        Consulta produtos por nome.

        Permite buscar produtos pelo nome e exibe as informações do produto encontrado,
        incluindo a quantidade disponível.

        :return: None
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
            CriarTabelas.exibir_tabela(item)


        print("\n\n")
        input("Pressione enter para voltar")
        Sistema.limpar_tela()
        return

    def _fazer_pedido(self):
        """
        Permite fazer um pedido de produtos.

        Exibe todos os produtos disponíveis (status "ativo"), solicita o ID do produto
        e a quantidade desejada, verifica se há estoque suficiente e cria um pedido
        com status "Em Análise".

        :return: None
        """
        while True:
            print("PRODUTOS DISPONÍVEIS: \n")

            for produto in self.produtos.listar():
                if produto["status"] == "ativo":
                    del produto["id_doador"]
                    del produto["id_responsavel"]
                    del produto["status"]
                    CriarTabelas.exibir_tabela(produto)


            try:
                print("\n")
                escolha = int(input("Digite o número do id do produto desejado ou '0' para voltar: "))

                if escolha == 0:
                    Sistema.limpar_tela()
                    return

                for pedido in self.pedidos.listar():
                    for produto in pedido["pedido"]:
                        if escolha == produto["id"]:
                            Sistema.limpar_tela()
                            print("Pedido ja enviado")
                            time.sleep(1.5)
                            Sistema.limpar_tela()
                            return

                for itens in self.produtos.listar():
                    if escolha == itens["id"]:
                        pegar_quantidade = int(input("digite a quantidade desejada: "))

                        if pegar_quantidade > itens["quantidade"]:
                            Sistema.limpar_tela()
                            print("Quantidade excedeu a quantidade total de produtos.")
                            time.sleep(1.5)
                            Sistema.limpar_tela()
                            continue



                        del itens["quantidade"]
                        del itens["id_doador"]
                        del itens["id_responsavel"]
                        itens["quantidade_pedida"] = pegar_quantidade
                        itens["solicitante"] = self.usuario["nome"]
                        itens["cpf_solicitante"] = self.usuario["cpf"]
                        itens["status"] = "Em Análise"

                        chave_pedido = f"pedido"
                        pedido = {chave_pedido: []}

                        pedido[chave_pedido].append(itens)


                        self.pedidos.cadastrar(pedido)
                        Sistema.limpar_tela()
                        print("Pedido enviado")
                        time.sleep(1.5)
                        Sistema.limpar_tela()
                        break

                    # else:
                        # print("Identificador não encontrado")


            except ValueError:
                Sistema.limpar_tela()
                continue

    def _status_pedidos(self):
        """
        Exibe o status dos pedidos do solicitante.

        Lista todos os pedidos do solicitante logado, mostrando pedidos em análise,
        aprovados e reprovados.

        :return: None
        """
        print("Solicitações enviadas: \n\n")

        meus_pedidos = self.pedidos.listar()

        for pedido in meus_pedidos:
            for produto in pedido["pedido"]:
                if produto["cpf_solicitante"] == self.usuario["cpf"]:
                    CriarTabelas.exibir_tabela(produto)

        for aprovado in self.produtos_aprovados.listar():
            for produto in aprovado["pedido"]:
                if produto["cpf_solicitante"] == self.usuario["cpf"]:
                    CriarTabelas.exibir_tabela(produto)

        for reprovado in self.produtos_reprovados.listar():
            for produto in reprovado["pedido"]:
                if produto["cpf_solicitante"] == self.usuario["cpf"]:
                    CriarTabelas.exibir_tabela(produto)


        input("\nTecle enter para voltar")
        Sistema.limpar_tela()
        return





