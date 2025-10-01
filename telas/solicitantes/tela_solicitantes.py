import time
from usuarios.gerenciador import Gerenciador
from utils.sistema.sistema import limpar_tela
from utils.exibir_tabela.exibir import exibir_tabela
class TelaSolicitantes:

    def __init__(self, usuario):
        self.usuario = usuario
        self.json_pedidos = "jsons/solicitacoes/pedidos.json"
        self.json_produtos = "jsons/produtos/produtos.json"
        self.json_aprovados = "jsons/solicitacoes/aprovados.json"
        self.json_reprovados = "jsons/solicitacoes/reprovados.json"
        self.produtos = Gerenciador(self.json_produtos)
        self.pedidos = Gerenciador(self.json_pedidos)
        self.produtos_aprovados = Gerenciador(self.json_aprovados)
        self.produtos_reprovados = Gerenciador(self.json_reprovados)
        self.iniciar = True
        self.categorias = ["Vestuário", "Medicamentos", "Alimentícios"]

    def mostrar(self):

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
                    limpar_tela()
                    self._consultar_produtos()
                    continue

                elif opcao == 2:
                    limpar_tela()
                    self._fazer_pedido()
                    continue

                elif opcao == 3:
                    limpar_tela()
                    self._status_pedidos()
                    continue

                elif opcao == 0:
                    if opcao == 0:
                        limpar_tela()
                        print("Voltando...")
                        time.sleep(1.2)
                        limpar_tela()
                        return
                else:
                    limpar_tela()
                    continue
            except ValueError:
                limpar_tela()
                continue

    def _consultar_produtos(self):
        """
        Mostra a tela de consultar produtos no terminal.

        Exibe todos os produtos disponíveis e permite ao usuário digitar o nome do produto desejável.
        Se o produto for encontrado, ele exibe as informações do produto e as quantidades disponíveis.
        Se o produto não for encontrado, ele exibe uma mensagem de erro e volta para a tela inicial.
        """

        digitar_produto = input("Digite o nome do produto desejável: ").title()

        consultar_produto = self.produtos.consulta(digitar_produto)

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

    def _fazer_pedido(self):

        """
        Mostra a tela de fazer pedido no terminal.

        Exibe todos os produtos disponíveis e permite ao usuário digitar o identificador do produto desejado.
        Se o produto for encontrado, ele exibe as informações do produto e as quantidades disponíveis.
        Se o produto não for encontrado, ele exibe uma mensagem de erro e volta para a tela inicial.
        """
        while True:
            print("PRODUTOS DISPONÍVEIS: \n")

            for produto in self.produtos.listar():
                produto["quantidade_disponivel"] = produto["quantidade"]
                del produto["quantidade"]
                del produto["id_doador"]
                del produto["id_responsavel"]
                exibir_tabela(produto)


            try:
                print("\n")
                pegar_identificador = int(input("Digite o número do identificador do produto desejado ou '0' para voltar: "))

                if pegar_identificador == 0:
                    limpar_tela()
                    return



                for itens in self.produtos.listar():
                    if pegar_identificador in self.pedidos.listar():
                        print("Pedido já enviado")
                        time.sleep(1.5)
                        limpar_tela()
                        continue

                    if pegar_identificador == itens["id"]:
                        pegar_quantidade = int(input("digite a quantidade desejada: "))

                        if pegar_quantidade > itens["quantidade"]:
                            limpar_tela()
                            print("Quantidade excedeu a quantidade total de produtos.")
                            time.sleep(1.5)
                            limpar_tela()
                            continue



                        del itens["quantidade"]
                        del itens["id_doador"]
                        del itens["id_responsavel"]
                        itens["quantidade_pedida"] = pegar_quantidade
                        itens["id_solicitante"] = self.usuario["id"]
                        itens["status"] = "Em Análise"

                        chave_pedido = f"pedido"
                        pedido = {chave_pedido: []}

                        pedido[chave_pedido].append(itens)


                        self.pedidos.cadastrar(pedido)
                        limpar_tela()
                        print("Pedido enviado")
                        time.sleep(1.5)
                        limpar_tela()
                        break

                    # else:
                        # print("Identificador não encontrado")


            except ValueError:
                limpar_tela()
                continue

    def _status_pedidos(self):
        """
        Mostra a tela de status de pedidos solicitados no terminal.

        Aqui o usuário apenas visualiza se o pedido dele está ainda em análise ou se foi aprovado ou reprovado.
        """
        print("Solicitações enviadas: \n\n")

        meus_pedidos = self.pedidos.listar()

        for pedido in meus_pedidos:
            for produto in pedido["pedido"]:
                if produto["id_solicitante"] == self.usuario["id"]:
                    exibir_tabela(produto)

        for aprovado in self.produtos_aprovados.listar():
            for produto in aprovado["pedido"]:
                if produto["id_solicitante"] == self.usuario["id"]:
                    exibir_tabela(produto)

        for reprovado in self.produtos_reprovados.listar():
            for produto in reprovado["pedido"]:
                if produto["id_solicitante"] == self.usuario["id"]:
                    exibir_tabela(produto)


        input("\nTecle enter para voltar")
        limpar_tela()
        return






# tela = TelaSolicitantes()
# tela.mostrar()
