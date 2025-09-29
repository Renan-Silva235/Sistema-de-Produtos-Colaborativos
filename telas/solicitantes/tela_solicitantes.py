import time
from usuarios.gerenciador import Gerenciador
from utils.sistema.sistema import limpar_tela
from utils.exibir_tabela.exibir import exibir_tabela
class TelaSolicitantes:

    def __init__(self, usuario):
        self.usuario = usuario
        self.json_pedidos = "jsons/solicitacoes/pedidos.json"
        self.json_produtos = "jsons/produtos/produtos.json"
        self.produtos = Gerenciador(self.json_produtos)
        self.pedidos = Gerenciador(self.json_pedidos)
        self.iniciar = True
        self.categorias = ["Vestuário", "Medicamentos", "Alimentícios"]

        self.vestuario = {
                            "identificador": None,
                            "categoria": None,
                            "nome_produto": None,
                            "marca": None,
                            "cor": None,
                            "tamanho": None,
                            "quantidade_disponivel": None,
                        }

        self.medicamentos = {
                            "identificador": None,
                            "categoria": None,
                            "nome_medicamento": None,
                            "dosagem": None,
                            "validade": None,
                            "quantidade_disponivel": None,
                            }

        self.alimentos = {
                            "identificador": None,
                            "categoria": None,
                            "nome_alimento": None,
                            "peso": None,
                            "validade": None,
                            "quantidade_disponivel": None,
                        }


    def mostrar(self):

        print(f"Solicitante: {self.usuario["nome"]}\n\n")
        while self.iniciar:
            print("""
                  Seja Bem-Vindo(a) ao nosso sistema de Doações, aqui você poderá consultar alguns produtos que estão disponíveis
                  para doação e fazer pedidos. Seus pedidos serão avaliados pela nossa equipe de Administração, caso seja aprovado ou não
                  você será notificado(a) pela aba pedidos. Em caso de aprovação, seu pedido será entregue no seu endereço cadastrado.\n\n""")

            print("1 - Consultar Produto")
            print("2 - Fazer pedido")
            print("3 - pedidos")
            print("0 - voltar\n")

            try:
                opcao = int(input("Digite uma das opções acima: "))

                if opcao == 1:
                    limpar_tela()
                    digitar_produto = input("Digite o nome do produto desejável: ").title()

                    consultar_produto = self.produtos.consulta(digitar_produto)

                    if not consultar_produto:
                        print("Nenhum Produto encontrado\n\n")
                        continue

                    for item in consultar_produto:
                        if item["categoria"] == self.categorias[0]:
                            self.vestuario["identificador"] = item["id"]
                            self.vestuario["categoria"] = item["categoria"]
                            self.vestuario["nome_produto"] = item["nome_produto"]
                            self.vestuario["marca"] = item["marca"]
                            self.vestuario["cor"] = item["cor"]
                            self.vestuario["tamanho"] = item["tamanho"]
                            self.vestuario["quantidade_disponivel"] = item["quantidade"]
                            exibir_tabela(self.vestuario)

                        elif item["categoria"] == self.categorias[1]:
                            self.medicamentos["identificador"] = item["id"]
                            self.medicamentos["categoria"] = item["categoria"]
                            self.medicamentos["nome_medicamento"] = item["nome_medicamento"]
                            self.medicamentos["dosagem"] = item["dosagem"]
                            self.medicamentos["validade"] = item["validade"]
                            self.medicamentos["quantidade_disponivel"] = item["quantidade_disponivel"]
                            exibir_tabela(self.medicamentos)

                        elif item["categoria"] == self.categorias[2]:
                            self.alimentos["identificador"] = item["id"]
                            self.alimentos["categoria"] = item["categoria"]
                            self.alimentos["nome_alimento"] = item["nome_alimento"]
                            self.alimentos["peso"] = item["peso"]
                            self.alimentos["validade"] = item["validade"]
                            self.alimentos["quantidade_disponivel"] = item["quantidade"]
                            exibir_tabela(self.alimentos)


                elif opcao == 2:
                    limpar_tela()
                    while True:
                        print("PRODUTOS DISPONÍVEIS: \n")

                        for produto in self.produtos.listar():
                            if produto["categoria"] == self.categorias[0]:
                                self.vestuario["identificador"] = produto["id"]
                                self.vestuario["categoria"] = produto["categoria"]
                                self.vestuario["nome_produto"] = produto["nome_produto"]
                                self.vestuario["marca"] = produto["marca"]
                                self.vestuario["cor"] = produto["cor"]
                                self.vestuario["tamanho"] = produto["tamanho"]
                                self.vestuario["quantidade_disponivel"] = produto["quantidade"]
                                exibir_tabela(self.vestuario)

                            elif produto["categoria"] == self.categorias[1]:
                                self.medicamentos["identificador"] = produto["id"]
                                self.medicamentos["categoria"] = produto["categoria"]
                                self.medicamentos["nome_medicamento"] = produto["nome_medicamento"]
                                self.medicamentos["dosagem"] = produto["dosagem"]
                                self.medicamentos["validade"] = produto["validade"]
                                self.medicamentos["quantidade_disponivel"] = produto["quantidade"]
                                exibir_tabela(self.medicamentos)

                            elif produto["categoria"] == self.categorias[2]:
                                self.alimentos["identificador"] = produto["id"]
                                self.alimentos["categoria"] = produto["categoria"]
                                self.alimentos["nome_alimento"] = produto["nome_alimento"]
                                self.alimentos["peso"] = produto["peso"]
                                self.alimentos["validade"] = produto["validade"]
                                self.alimentos["quantidade_disponivel"] = produto["quantidade"]
                                exibir_tabela(self.alimentos)


                        try:
                            print("\n")
                            pegar_identificador = int(input("Digite o número do identificador do produto desejado ou '0' para voltar: "))

                            if pegar_identificador == 0:
                                limpar_tela()
                                break

                            for itens in self.produtos.listar():

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

                elif opcao == 3:
                    limpar_tela()
                    print("Solicitações enviadas: \n\n")

                    meus_pedidos = self.pedidos.listar()

                    for pedido in meus_pedidos:
                        for produto in pedido["pedido"]:
                            if produto["id_solicitante"] == self.usuario["id"]:
                                exibir_tabela(produto)

                    input("\nTecle enter para voltar")
                    limpar_tela()

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



# tela = TelaSolicitantes()
# tela.mostrar()
