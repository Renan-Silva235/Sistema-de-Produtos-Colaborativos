import time
import pandas as pd
from utils.pegar_dados.pegar_dados_usuario import pegar_dados_solicitantes
from utils.sistema.sistema import limpar_tela
from conexoes.crud import cadastrar, consulta
from validacoes.validacao import Validacoes

class TelaCadastrarSolicitante:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.json_solicitante = "jsons/dados_pessoais/dados_solicitantes.json"
    def mostrar(self):
        """Esse método exibe a tela de cadastro de Doador no terminal."""

        try:
            continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
            if continuar_ou_não == 2:
                self.gerenciador.mudar_tela("TelaMenuCadastro")
                return
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarSolicitante")
            return

        dados_usuario = pegar_dados_solicitantes()

        if not dados_usuario:
            self.gerenciador.mudar_tela("TelaCadastrarSolicitante")
            return

        limpar_tela()


        loop = True
        while loop:
            print("VISUALIZAÇÃO:")
            print()
            print()
            print("Dados do candidato:")
            print()
            print(pd.DataFrame([dados_usuario]).to_string(index=False))
            print()
            print()
            condicao = input("Deseja realmente salvar esse usuário? (s/n): ").lower()

            if condicao not in ["s", "n"]:
                limpar_tela()
                continue

            elif condicao == "s":
                limpar_tela()
                consultar = consulta(self.json_solicitante)
                validar = Validacoes.validar_cadastro_usuario(self.json_solicitante, dados_usuario, consultar)

                if validar:
                    print("Usuário já está cadastrado no sistema.")
                    time.sleep(1.5)
                    limpar_tela()
                    break

                cadastrar(self.json_solicitante, dados_usuario)
                print("Usuário Cadastrado com Sucesso")
                time.sleep(1.5)
                limpar_tela()
                break
            else:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarSolicitante")
                time.sleep(1.5)
                break


        limpar_tela()
        self.gerenciador.mudar_tela("TelaCadastrarSolicitante")
        return
