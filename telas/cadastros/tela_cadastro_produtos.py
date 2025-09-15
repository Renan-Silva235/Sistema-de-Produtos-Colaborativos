import time
import pandas as pd
from utils.pegar_dados.pegar_dados_produtos import pegar_dados_alimenticios, pegar_dados_vestuario, pegar_dados_domestico
from utils.sistema.sistema import limpar_tela
from conexoes.crud import consulta, cadastrar
from validacoes.validacao import Validacoes
from utils.alteracoes.alterar import Alteracoes

class TelaCadastrarProdutos:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.alterar = Alteracoes()
        self.json_domestico = "jsons/categorias/domesticos.json"
        self.json_alimentos = "jsons/categorias/alimentos.json"
        self.json_vestuario = "jsons/categorias/vestuario.json"

    def mostrar(self):
        """Esse método exibe a tela de cadastro de produtos no terminal."""

        try:
            continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
            if continuar_ou_não == 2:
                self.gerenciador.mudar_tela("TelaAdministrador")
                return
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")
            return

        print("INFORME AS INFORMAÇÕES DO PRODUTO DOADO:")

        categorias = ["vestuário", "doméstico", "alimenticio"]

        print(f"""Informe a categoria do produto:
                1- {categorias[0]}
                2- {categorias[1]}
                3- {categorias[2]}
              """)

        try:
            opcao_categoria = int(input("Digite a opção corresponde a categoria do produto que você quer cadastrar: "))
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")

        if opcao_categoria not in [1,2,3]:
            print("opção inválida")
            time.sleep(1)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")

        if opcao_categoria == 1:
            produtos = pegar_dados_vestuario()
        elif opcao_categoria == 2:
            produtos = pegar_dados_domestico()
        else:
            produtos = pegar_dados_alimenticios()

        if not produtos:
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")
            return

        limpar_tela()


        while True:
            cpf = input("Informe o cpf do Doador: ")

            if not Validacoes.validar_cpf(cpf):
                print("CPF inválido")
                continue
            break

        todos_doadores = consulta("jsons/dados_pessoais/dados_doadores.json")

        achou = False
        for doador in todos_doadores:
            if doador["cpf"] == cpf:
                achou = True
                break
            else:
                achou = False

        if achou:
            doador_encontrado = doador
        else:
            limpar_tela()
            print("Doador não foi localizado no sistema")
            time.sleep(1.5)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")

        while True:
            print("VISUALIZAÇÃO:")
            print()
            print()
            print("Dados do Doador:")
            print(pd.DataFrame([doador_encontrado]).to_string(index=False))
            print()
            print("---------------------------------------------------------------")
            print()
            print("Dados do Produto Doado:")
            print()
            print(pd.DataFrame([produtos]).to_string(index=False))
            print()


            condicao = input("Deseja realmente salvar esse produto? (s/n): ").lower()

            if condicao not in ["s", "n"]:
                limpar_tela()
                continue

            elif condicao == "s":

                if opcao_categoria == 1:
                    limpar_tela()
                    consultar = consulta(self.json_vestuario)
                    validar = Validacoes.validar_cadastro_produto(self.json_vestuario, produtos, consultar)

                    if validar:
                        print("Produto já está cadastrado no sistema.")
                        print("Foi atualizado o número de quantidades do produto.")
                        produtos["id_doadores"].append(doador_encontrado["id"])
                        self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                        self.alterar.alterar_produto_existente(self.json_vestuario, validar, produtos['quantidade'], doador_encontrado["id"])
                        break

                    produtos["id_doadores"].append(doador_encontrado["id"])
                    self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                    cadastrar(self.json_vestuario, produtos)
                    break

                elif opcao_categoria == 2:
                    limpar_tela()
                    consultar = consulta(self.json_domestico)
                    validar = Validacoes.validar_cadastro_produto(self.json_domestico, produtos, consultar)

                    if validar:
                        print("Produto já está cadastrado no sistema.")
                        print("Foi atualizado o número de quantidades do produto.")
                        produtos["id_doadores"].append(doador_encontrado["id"])
                        self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                        self.alterar.alterar_produto_existente(self.json_domestico, validar, produtos["quantidade"], doador_encontrado["id"])
                        break

                    produtos["id_doadores"].append(doador_encontrado["id"])
                    self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                    cadastrar(self.json_domestico, produtos)
                    break

                else:
                    limpar_tela()
                    consultar = consulta(self.json_alimentos)
                    validar = Validacoes.validar_cadastro_produto(self.json_alimentos, produtos, consultar)

                    if validar:
                        print("Produto já está cadastrado no sistema.")
                        print("Foi atualizado o número de quantidades do produto.")
                        produtos["id_doadores"].append(doador_encontrado["id"])
                        self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                        self.alterar.alterar_produto_existente(self.json_alimentos, validar, produtos['quantidade'], doador_encontrado["id"])
                        break

                    produtos["id_doadores"].append(doador_encontrado["id"])
                    self.alterar.alterar_total_doacoes(cpf, produtos["quantidade"])
                    cadastrar(self.json_alimentos, produtos)
                    break


            else:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarProdutos")
                time.sleep(1)
                break


        time.sleep(5)
        limpar_tela()

        self.gerenciador.mudar_tela("TelaCadastrarProdutos")
