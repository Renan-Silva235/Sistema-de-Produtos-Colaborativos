import time
import pandas as pd
from utils.pegar_dados.pegar_dados_usuario import pegar_dados_voluntario
from utils.sistema.sistema import limpar_tela
from conexoes.crud import cadastrar, consulta
from validacoes.validacao import Validacoes

class TelaCadastrarFuncionarioVoluntario:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.json_funcionario = "jsons/dados_pessoais/dados_funcionarios.json"
    def mostrar(self):
        """Tela de cadastro de Funcionário ou Voluntário"""

        try:
            continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
            if continuar_ou_não == 2:
                self.gerenciador.mudar_tela("TelaMenuCadastro")
                return
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")
            return

        print("INFORME AS INFORMAÇÕES DO PRODUTO DOADO:")
        print()
        niveis = ["Administrador", "Voluntário", "Solicitante"]


        print(f"""Informe a categoria do produto:
                1- {niveis[0]}
                2- {niveis[1]}
                3- {niveis[2]}
              """)

        try:
            opcao_nivel = int(input("Digite a opção corresponde ao nível: "))
        except ValueError:
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")

        if opcao_nivel not in [1,2,3]:
            print("opção inválida")
            time.sleep(1)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")

        dados_usuario = pegar_dados_voluntario()

        if not dados_usuario:
            self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")
            return

        dados_usuario["nivel"] = niveis[opcao_nivel - 1]

        limpar_tela()

        while True:
            print("VISUALIZAÇÃO:")
            print()
            print()
            print("Dados do candidato:")
            print()
            print(pd.DataFrame([dados_usuario]).to_string(index=False))
            print()
            print()
            condicao = input("Deseja realmente salvar este registro? (s/n): ").lower()

            if condicao not in ["s", "n"]:
                limpar_tela()
                continue

            elif condicao == "s":
                limpar_tela()
                consultar = consulta(self.json_funcionario)
                validar = Validacoes.validar_cadastro_usuario(self.json_funcionario, dados_usuario, consultar)

                if validar:
                    print("Funcionário / Voluntário já está cadastrado no sistema.")
                    time.sleep(1.5)
                    limpar_tela()
                    break

                cadastrar(self.json_funcionario, dados_usuario)
                print("Funcionário/Voluntário cadastrado com sucesso")
                time.sleep(1.5)
                limpar_tela()
                break
            else:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")
                time.sleep(1)
                return

        limpar_tela()
        self.gerenciador.mudar_tela("TelaCadastrarFuncionarioVoluntario")
