from utils.sistema.sistema import limpar_tela
from usuarios.gerenciador import Gerenciador
from utils.exibir_tabela.exibir import exibir_tabela
class TelaPedidos:
    def __init__(self):
        self.json_pedidos = "jsons/solicitacoes/pedidos.json"
        self.pedidos = Gerenciador(self.json_pedidos)

    def mostrar(self):
        print("PEDIDOS SOLICITADOS: \n\n")

        categorias = ["Vestuário", "Medicamentos", "Alimentícios"]

        for pedido in self.pedidos.listar():
            if pedido["categoria"] == categorias[0]:
                produto = {
                    "identificador": pedido["id"],
                    "categoria": pedido["categoria"],
                    "nome_produto": pedido["nome_produto"],
                    "marca": pedido["marca"],
                    "cor": pedido["cor"],
                    "tamanho": pedido["tamanho"]
                }
                exibir_tabela(produto)
            elif pedido["categoria"] == categorias[1]:
                produto = {
                    "identificador": pedido["id"],
                    "categoria": pedido["categoria"],
                    "nome_medicamento": pedido["nome_medicamento"],
                    "apresentacao": pedido["apresentacao"],
                    "dosagem": pedido["dosagem"],
                    "validade": pedido["validade"]
                }

                exibir_tabela(produto)
            elif pedido["categoria"] == categorias[2]:
                produto = {
                    "identificador": pedido["id"],
                    "categoria": pedido["categoria"],
                    "nome_alimento": pedido["nome_alimento"],
                    "peso": pedido["peso"],
                    "validade": pedido["validade"]
                }

                exibir_tabela(produto)



tela = TelaPedidos()
tela.mostrar()
