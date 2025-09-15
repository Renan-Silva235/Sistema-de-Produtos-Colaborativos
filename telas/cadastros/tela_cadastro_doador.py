import time
import pandas as pd
from utils.pegar_dados.pegar_dados_usuario import pegar_dados_doadores
from utils.sistema.sistema import limpar_tela
from conexoes.crud import cadastrar, consulta
from validacoes.validacao import Validacoes

class TelaCadastrarDoador:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.json_doadores = "jsons/dados_pessoais/dados_doadores.json"

    def mostrar(self):
        """Esse método exibe a tela de cadastro de produtos no terminal."""

        try:
            continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
            if continuar_ou_não == 2:
                self.gerenciador.mudar_tela("TelaMenuCadastro")
                return
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarDoador")
            return

        print("INFORME OS DADOS DO DOADOR:")
        dados_usuario = pegar_dados_doadores()

        if not dados_usuario:
            self.gerenciador.mudar_tela("TelaCadastrarDoador")
            return

        limpar_tela()

        loop = True
        while loop:
            print("VISUALIZAÇÃO:")
            print()
            print()
            print("Dados do Doador:")
            print(pd.DataFrame([dados_usuario]).to_string(index=False))
            print()
            print("---------------------------------------------------------------")


            condicao = input("Deseja realmente salvar esse doador? (s/n): ").lower()

            if condicao not in ["s", "n"]:
                limpar_tela()
                continue

            elif condicao == "s":
                limpar_tela()
                consultar = consulta(self.json_doadores)
                validar = Validacoes.validar_cadastro_usuario(self.json_doadores, dados_usuario, consultar)

                if validar:
                    print("Doador já está cadastrado no sistema.")
                    time.sleep(5)
                    limpar_tela()
                    break

                cadastrar(self.json_doadores, dados_usuario)
                time.sleep(1.5)
                limpar_tela()
                break
            else:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarDoador")
                time.sleep(1.5)
                break


        limpar_tela()
        self.gerenciador.mudar_tela("TelaCadastrarDoador")
