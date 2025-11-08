import time
from produto.categorias import Alimentos, Medicamentos, Vestuario
from usuarios.doadores import Doacao
from crud.crud import Crud
from utils.sistema.sistema import Sistema
from validacoes.validacoes_produtos import ValidacoesProdutos
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.alteracoes.alterar import Alteracoes
from utils.exibir_tabela.exibir import CriarTabelas


class TelaCadastrarProdutos:
    """
    Classe responsável pela tela de cadastro de produtos.

    Permite cadastrar novos produtos no sistema (Alimentícios, Medicamentos ou Vestuário),
    associando-os a um doador. Verifica se o produto já está cadastrado antes de salvar.
    """

    def __init__(self, usuario):
        """
        Inicializa a tela de cadastro de produtos.

        :param usuario: Dicionário com os dados do usuário responsável pelo cadastro
        """
        self.usuario = usuario
        self.alterar = Alteracoes()
        self.json_produtos = "jsons/produtos/produtos.json"
        self.json_doador = "jsons/dados_pessoais/doadores.json"
        self.crud = Crud(self.json_produtos)
        self.iniciar = True

    def mostrar(self):
        """
        Exibe a tela de cadastro de produtos no terminal.

        Solicita a categoria do produto, os dados específicos da categoria,
        valida as informações, associa a um doador, exibe uma pré-visualização
        e permite confirmar o cadastro. Se o produto já existir, atualiza a quantidade.

        :return: None
        """

        while self.iniciar:
            try:
                continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
                if continuar_ou_não not in [1, 2]:
                    Sistema.limpar_tela()
                    continue

                elif continuar_ou_não == 2:
                    Sistema.limpar_tela()
                    print("Voltando..")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return

            except ValueError:
                Sistema.limpar_tela()
                continue

            print("\n\nINFORME AS INFORMAÇÕES DO PRODUTO DOADO:\n\n")

            categorias = ["vestuário", "medicamentos", "alimenticio"]

            print(f"""Informe a categoria do produto:
                    1- {categorias[0]}
                    2- {categorias[1]}
                    3- {categorias[2]}
                """)

            try:
                opcao_categoria = int(input("Digite a opção corresponde a categoria do produto que você quer cadastrar: "))
                if opcao_categoria not in [1,2,3]:
                    print("opção inválida")
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue


            if opcao_categoria == 1:

                try:
                    tipo_roupa = input("Digite o tipo da roupa (meia, calça, blusa, etc): ").title()
                    marca = input("Marca do Produto: ").title()
                    cor = input("Cor do Produto: ").title()
                    tamanho = input("Defina os seguintes tamanhos: \n"
                                    "- utilize números para o tamanho dos Calçados \n" \
                                    "- Utilize os as medidas (P, M, G, GG) para roupas:\n" \
                                    "TAMANHO: ").upper()
                    ValidacoesProdutos.validar_tamanho_vestuario(tamanho)
                    quantidade = int(input("Digite a quantidade: "))

                except ValueError as erro:
                    print(erro)
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue

                produto = Vestuario(nome_produto=tipo_roupa, marca=marca, cor=cor, tamanho=tamanho, quantidade=quantidade)

            elif opcao_categoria == 2:
                try:
                    nome_medicamento = input("Nome do medicamento: ").title()
                    dosagem = input("Dosagem: ex(500 mg, 100mg): ").title()
                    validade = input("Digite a validade do produto utilizando '/' para separar dia/mês/ano: ")
                    ValidacoesProdutos.validar_formato_data(validade)
                    quantidade = int(input("Quantidade: "))
                except ValueError as erro:
                    print(erro)
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue

                produto = Medicamentos(nome_medicamento=nome_medicamento,
                                       dosagem=dosagem,
                                       validade=validade,
                                       quantidade=quantidade)

            else:
                try:
                    alimento = input("Digite o nome do produto: ").title()
                    peso = input("Digite o peso do produto (Acrescente a unidade de medida: Kg, G, L, Ml): ").title()
                    ValidacoesProdutos.validar_peso(peso)

                    validade = input("Digite a validade do produto utilizando '/' para separar dia/mês/ano: ")
                    ValidacoesProdutos.validar_formato_data(validade)

                    quantidade = int(input("Digite a quantidade total de produtos: "))
                except ValueError as erro:
                    print(erro)
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue

                produto = Alimentos(nome_alimento=alimento, peso=peso, validade=validade, quantidade=quantidade)

            Sistema.limpar_tela()

            iniciar_loop = True
            while iniciar_loop:
                try:
                    cpf = input("Informe o cpf do Doador ou '0' para voltar: ")
                    if len(cpf) == 1 and cpf == '0':
                        iniciar_loop = False
                        Sistema.limpar_tela()
                        print("Voltando...")
                        time.sleep(1.5)
                        Sistema.limpar_tela()
                        return
                    ValidacoesUsuario.validar_cpf(cpf)
                    todos_doadores = Crud(self.json_doador).listar()
                except ValueError as erro:
                    print(erro)
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue

                doador_encontrado = None
                for doador in todos_doadores:
                    if doador["cpf"] == cpf:
                        doador_encontrado = doador
                        iniciar_loop = False

                if doador_encontrado is None:
                    print("Nenhum doador encontrado")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue


            Sistema.limpar_tela()

            iniciar_loop = True
            while iniciar_loop:
                print("VISUALIZAÇÃO:\n\n")
                print("Dados do Doador:\n\n")
                CriarTabelas.exibir_tabela(doador_encontrado, titulo="Doador")
                print("\n")
                print("---------------------------------------------------------------\n\n")
                print("Dados do Produto Doado:\n\n")
                CriarTabelas.exibir_tabela(produto.objeto(), titulo="Produto")

                condicao = input("\n\nDeseja realmente salvar esse produto? (s/n): ").lower()

                if condicao not in ["s", "n"]:
                    Sistema.limpar_tela()
                    continue

                elif condicao == "s":

                    Sistema.limpar_tela()
                    validar = ValidacoesProdutos.validar_cadastro_produto(self.json_produtos, produto.objeto(), self.crud.listar())

                    if validar:
                        print("Produto já está cadastrado no sistema.")
                        print("Foi atualizado o número de quantidades do produto.")

                        # produto.objeto()["id_doador"].append(doador_encontrado["id"])
                        # produto.objeto()["id_doador"].append(doador_encontrado["id"])
                        self.alterar.alterar_total_doacoes(cpf, produto.objeto()["quantidade"])
                        self.alterar.alterar_produto_existente(self.json_produtos, validar, produto.objeto()['quantidade'], doador_encontrado["id"])
                        time.sleep(1.5)
                        Sistema.limpar_tela()
                        iniciar_loop = False
                        continue

                    doacao = Doacao(doador_encontrado, produto.objeto(), self.usuario)
                    self.alterar.alterar_total_doacoes(cpf, produto.objeto()["quantidade"])
                    self.crud.cadastrar(doacao.objeto())
                    Sistema.limpar_tela()
                    print("Produto Cadastrado com Sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    iniciar_loop = False
                    continue

                else:
                    Sistema.limpar_tela()
                    iniciar_loop = False
                    continue

            Sistema.limpar_tela()
            continue
