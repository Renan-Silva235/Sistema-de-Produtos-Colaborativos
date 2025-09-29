import time
from usuarios.gerenciador import Gerenciador
from utils.sistema.sistema import limpar_tela
from utils.exibir_tabela.exibir import exibir_tabela
class TelaSolicitantes:

    def __init__(self, usuario):
        self.usuario = usuario
        self.json_produtos = "jsons/produtos/produtos.json"
        self.produtos = Gerenciador(self.json_produtos)
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

        while self.iniciar:
            print(f"Solicitante: {self.usuario["nome"]}\n\n")
            print("1 - Consultar Produto")
            print("2 - Fazer pedido")
            print("0 - voltar")

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
