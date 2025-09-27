import pandas as pd
import time
from tabulate import tabulate
from utils.sistema.sistema import limpar_tela

class TelaControleDeEstoque:

    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.produtos_alimenticios = pd.read_json("jsons/categorias/alimentos.json").drop(columns="id_doadores", errors="ignore")
        self.produtos_domesticos = pd.read_json("jsons/categorias/domesticos.json").drop(columns="id_doadores", errors="ignore")
        self.produtos_vestuario = pd.read_json("jsons/categorias/vestuario.json").drop(columns="id_doadores", errors="ignore")

    def mostrar(self):
        msg_produto_disponiveis = "PRODUTOS DISPONÍVEIS NO ESTOQUE:\n\n"
        print(msg_produto_disponiveis)
        print("""
              Opções de Visualização: \n\n
         1- mostrar produtos alimenticios
         2- mostrar produtos domesticos
         3- mostrar produtos de vestimenta
         4- mostrar tudo
         0- Voltar \n\n""")



        while True:
            categoria = int(input("Digite uma das opções acima: "))

            if categoria == 1:
                limpar_tela()
                print(msg_produto_disponiveis)
                print(tabulate(self.produtos_alimenticios, headers='keys', tablefmt='pretty', showindex=False))
                break
            elif categoria == 2:
                limpar_tela()
                print(msg_produto_disponiveis)
                print(tabulate(self.produtos_domesticos, headers='keys', tablefmt='pretty', showindex=False))
                break
            elif categoria == 3:
                limpar_tela()
                print(msg_produto_disponiveis)
                print(tabulate(self.produtos_vestuario, headers='keys', tablefmt='pretty', showindex=False))
                break
            elif categoria == 0:
                print("Opção Inválida")
                time.sleep(1.5)
                limpar_tela()
                continue




