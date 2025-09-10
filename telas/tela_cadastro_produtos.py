import time
from utils.pegar_dados import pegar_dados_alimenticios
from utils.sistema import limpar_tela
from funcao_salvar_json.salvarJson import salvarNoJson

class TelaCadastrarProdutos:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def mostrar(self):
        """Esse método exibe a tela de cadastro de produtos no terminal."""

        categorias = ["vestuario", "domestico", "alimenticio"]
        loop = True
        continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar a tela Admin: "))


        if continuar_ou_não == 2:
            self.gerenciador.mudar_tela("TelaAdministrador")

        print(f"""Informe a categoria do produto:
                1- {categorias[0]}
                2- {categorias[1]}
                3- {categorias[2]}
              """)

        opcao_categoria = int(input("Digite a opção corresponde a categoria do produto que você quer cadastrar: "))

        if opcao_categoria not in [1,2,3]:
            print("opção inválida")
            time.sleep(1)
            limpar_tela()
            self.gerenciador.mudar_tela("TelaCadastrarProdutos")


        if opcao_categoria == 3:
            produtos = pegar_dados_alimenticios()




        limpar_tela()
        print(f"""VISUALIZAÇÃO:

                {produtos}
            """)

        loop = True
        while loop:
            condicao = input("Deseja realmente salvar esse produto? (s/n): ").lower()

            if condicao not in ["s", "n"]:
                print("opção inválida")
                continue
            elif condicao == "s":
                if opcao_categoria == 3:
                    salvarNoJson("json/categorias/alimentos.json", produtos)
                    print("Produto cadastrado com sucesso")
                time.sleep(1)
                limpar_tela()
                break
            else:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarProdutos")

                time.sleep(1)
                break

        limpar_tela()
        self.gerenciador.mudar_tela("TelaCadastrarProdutos")
