import time
from crud.crud import Crud
from utils.sistema.sistema import Sistema
from utils.exibir_tabela.exibir import CriarTabelas
from tabulate import tabulate
from utils.alteracoes.alterar import Alteracoes
from datetime import datetime, timedelta


class TelaControleEstoque:
    """
    Classe responsável pela tela de controle de estoque.

    Fornece funcionalidades para gerenciar o estoque de produtos: listar, filtrar,
    consultar, registrar entradas/saídas, verificar baixa de estoque, alertas de validade,
    atualizar validade e ativar/inativar produtos.
    """

    def __init__(self):
        """
        Inicializa a tela de controle de estoque.
        """
        self.json_produtos = "jsons/produtos/produtos.json"
        self.crud = Crud(self.json_produtos)
        self.iniciar = True
        self.alterar = Alteracoes()

    def mostrar(self):
        """
        Exibe o menu principal de controle de estoque no terminal.

        Apresenta as opções disponíveis para gerenciamento do estoque e direciona
        para as funcionalidades específicas conforme a escolha do usuário.

        :return: None
        """
        while self.iniciar:
            # conta itens que vencem em 1 dia (alerta)
            try:
                alertas_um_dia = self._contar_alertas_um_dia()
            except Exception:
                alertas_um_dia = 0
            print("CONTROLE DE ESTOQUE:\n")
            print(f"""
                    1 - Listar estoque completo
                    2 - Filtrar por categoria
                    3 - Consultar produto
                    4 - Registrar entrada (adicionar quantidade)
                    5 - Registrar saída (retirar quantidade)
                    6 - Itens com baixa de estoque
                    7 - Alertas de validade próxima ou vencida ({alertas_um_dia})
                    8 - Atualizar validade do produto
                    9 - Ativar/Inativar produto
                    0 - Voltar
                """)

            try:
                opcao = int(input("Digite uma das opções acima: "))
            except ValueError:
                Sistema.limpar_tela()
                continue

            if opcao == 1:
                Sistema.limpar_tela()
                print("Executando listar_estoque()...")
                self.listar_estoque()
                input("\nPressione Enter para continuar...")
                Sistema.limpar_tela()
                continue
            elif opcao == 2:
                Sistema.limpar_tela()
                self.filtrar_por_categoria()
                continue
            elif opcao == 3:
                Sistema.limpar_tela()
                self._consultar_produto()
                continue
            elif opcao == 4:
                Sistema.limpar_tela()
                self.registrar_entrada()
                continue
            elif opcao == 5:
                Sistema.limpar_tela()
                self.registrar_saida()
                continue
            elif opcao == 6:
                Sistema.limpar_tela()
                self.itens_baixa_estoque()
                continue
            elif opcao == 7:
                Sistema.limpar_tela()
                self.alertas_validade()
                continue
            elif opcao == 8:
                Sistema.limpar_tela()
                self.atualizar_validade()
                continue
            elif opcao == 9:
                Sistema.limpar_tela()
                self.ativar_inativar_produto()
                continue
            elif opcao == 0:
                Sistema.limpar_tela()
                print("Voltando...")
                time.sleep(1.2)
                Sistema.limpar_tela()
                return
            else:
                Sistema.limpar_tela()
                continue

    def _nome_produto(self, produto):
        """
        Retorna o nome do produto baseado na sua categoria.

        :param produto: Dicionário com os dados do produto
        :return: String com o nome do produto ou "Sem nome" se não encontrado
        """
        categoria = produto.get("categoria", "")
        if categoria == "Medicamentos":
            valor = produto.get("nome_medicamento")
            return valor[0] if isinstance(valor, list) and valor else (valor or "Sem nome")
        if categoria == "Alimentícios":
            return produto.get("nome_alimento", "Sem nome")
        if categoria == "Vestuário":
            return produto.get("nome_produto", "Sem nome")
        return "Sem nome"

    def listar_estoque(self):
        """
        Lista todos os produtos do estoque.

        Exibe uma tabela com todos os produtos cadastrados no sistema.

        :return: None
        """
        produtos = self.crud.listar()
        if not produtos:
            print("Não há produto no estoque.")
            return

        for item in produtos:
            CriarTabelas.exibir_tabela(item)

    def filtrar_por_categoria(self):
        """
        Filtra e exibe produtos por categoria.

        Solicita a categoria desejada (Medicamentos, Alimentícios ou Vestuário)
        e exibe apenas os produtos dessa categoria.

        :return: None
        """
        print("1 - Medicamentos")
        print("2 - Alimentícios")
        print("3 - Vestuário")
        try:
            op = int(input("Selecione a categoria: "))
        except ValueError:
            Sistema.limpar_tela()
            return

        categoria = None
        if op == 1:
            categoria = "Medicamentos"
        elif op == 2:
            categoria = "Alimentícios"
        elif op == 3:
            categoria = "Vestuário"
        else:
            Sistema.limpar_tela()
            return

        itens = [i for i in self.crud.listar() if i.get("categoria") == categoria]
        if not itens:
            print(f"Nenhum item encontrado em '{categoria}'.")
            return

        CriarTabelas.exibir_tabela(itens)
        input("\nPressione Enter para continuar...")
        Sistema.limpar_tela()

    def _consultar_produto(self):
        """
        Consulta produtos por termo de busca.

        Permite buscar produtos por qualquer termo (nome, ID, etc.) e exibe
        os resultados encontrados.

        :return: None
        """
        try:
            pid = input("Informe o que deseja consultar: ")
        except ValueError:
            Sistema.limpar_tela()
            return

        produtos = self.crud.consultar(pid)
        if not produtos:
            print("Produto não encontrado.")
            return

        for produto in produtos:
            CriarTabelas.exibir_tabela(produto)
            input("\nPressione Enter para continuar...")
            Sistema.limpar_tela()

    def registrar_entrada(self):
        """
        Registra entrada de produtos no estoque.

        Adiciona uma quantidade ao estoque de um produto existente.

        :return: None
        """
        try:
            pid = int(input("ID do produto: "))
            qtd = int(input("Quantidade a adicionar: "))
        except ValueError:
            Sistema.limpar_tela()
            return
        if qtd <= 0:
            print("Quantidade deve ser positiva.")
            return

        itens = self.crud.listar()
        existe = any(item.get("id") == pid for item in itens)
        if not existe:
            print("Produto não encontrado.")
            return

        self.alterar.alterar_estoque(self.json_produtos, pid, qtd)
        print("Entrada registrada com sucesso.")

    def registrar_saida(self):
        """
        Registra saída de produtos do estoque.

        Remove uma quantidade do estoque de um produto existente.
        Verifica se há estoque suficiente antes de realizar a saída.

        :return: None
        """
        try:
            pid = int(input("ID do produto: "))
            qtd = int(input("Quantidade a retirar: "))
        except ValueError:
            Sistema.limpar_tela()
            return
        if qtd <= 0:
            print("Quantidade deve ser positiva.")
            return

        itens = self.crud.listar()
        alvo = None
        for item in itens:
            if item.get("id") == pid:
                alvo = item
                break
        if not alvo:
            print("Produto não encontrado.")
            return

        estoque_atual = alvo.get("quantidade", 0)
        if qtd > estoque_atual:
            print("Quantidade solicitada maior que o estoque atual.")
            return

        self.alterar.alterar_estoque(self.json_produtos, pid, -qtd)
        print("Saída registrada com sucesso.")

    # ...existing code...
    def itens_baixa_estoque(self):
        """
        Exibe produtos com baixa de estoque.

        Solicita um limite de quantidade e exibe todos os produtos
        com quantidade menor ou igual ao limite informado.

        :return: None
        """
        try:
            limite = int(input("Exibir itens com quantidade menor ou igual a: "))
        except ValueError:
            Sistema.limpar_tela()
            return

        itens_raw = self.crud.listar()
        itens = []
        for i in itens_raw:
            try:
                qtd = int(i.get("quantidade", 0))
            except Exception:
                # pula itens com quantidade inválida (ex.: None ou texto)
                continue
            if qtd <= limite:
                itens.append(i)

        if not itens:
            print("Nenhum item com baixa de estoque.")
            input("Tecle enter para voltar")
            Sistema.limpar_tela()
            return

        linhas = []
        for item in itens:
            linhas.append([
                item.get("id"),
                item.get("categoria", ""),
                self._nome_produto(item),
                int(item.get("quantidade", 0))
            ])
        print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Qtd"], tablefmt="fancy_grid"))
        input("\nPressione Enter para continuar...")
        Sistema.limpar_tela()
# ...existing code...

    def alertas_validade(self):
        """
        Exibe alertas de validade de produtos.

        Lista produtos vencidos e produtos com validade próxima (vencendo em 1 dia).
        Considera apenas produtos com status "ativo".

        :return: None
        """
        hoje = datetime.now().date()
        amanha = hoje + timedelta(days=1)

        itens = self.crud.listar()
        vencidos = []
        proximos = []

        for item in itens:
            if item.get("status") == "inativo":
                continue
            if item.get("status") == "ativo":

                validade_txt = item.get("validade")
                if not validade_txt:
                    continue
                try:
                    validade = datetime.strptime(validade_txt, "%d/%m/%Y").date()
                except Exception:
                    continue

                if validade < hoje:
                    vencidos.append(item)
                elif validade == amanha:
                    proximos.append(item)

        if not vencidos and not proximos:
            Sistema.limpar_tela()
            print("Nenhum produto vencido ou com validade próxima no período informado.")
            input("Tecle enter para voltar")
            Sistema.limpar_tela()
            return

        if vencidos:
            Sistema.limpar_tela()
            print("\n=== ITENS VENCIDOS ===")
            CriarTabelas.exibir_tabela(vencidos)
            input("Tecle enter para voltar")
            Sistema.limpar_tela()

        if proximos:
            Sistema.limpar_tela()
            print("\n=== ITENS COM VALIDADE PRÓXIMA ===")
            CriarTabelas.exibir_tabela(proximos)
            input("Tecle enter para voltar")
            Sistema.limpar_tela()

    def _contar_alertas_um_dia(self):
        """
        Conta quantos itens têm validade igual a amanhã (alerta de 1 dia).

        :return: Inteiro com a quantidade de produtos que vencem em 1 dia
        """
        amanha = (datetime.now() + timedelta(days=1)).date()
        itens = self.crud.listar()
        contador = 0
        for item in itens:
            if item.get("status") == "inativo":
                continue

            if item.get("status") == "ativo":

                validade_txt = item.get("validade")
                if not validade_txt:
                    continue
                try:
                    validade = datetime.strptime(validade_txt, "%d/%m/%Y").date()
                except Exception:
                    continue
                if validade == amanha:
                    contador += 1
        return contador

    def atualizar_validade(self):
        """
        Atualiza a validade de um produto.

        Solicita o ID do produto e a nova validade no formato dd/mm/aaaa,
        valida o formato e atualiza o produto.

        :return: None
        """
        try:
            pid = int(input("ID do produto: "))
        except ValueError:
            print("ID inválido.")
            return

        # Verifica se o produto existe
        itens = self.crud.listar()
        produto_existe = any(item.get("id") == pid for item in itens)
        if not produto_existe:
            print("Produto não encontrado.")
            return

        print("Digite a nova validade no formato dd/mm/aaaa:")
        nova_validade = input("Nova validade: ").strip()

        # Valida o formato da data
        try:
            datetime.strptime(nova_validade, "%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido. Use dd/mm/aaaa")
            return

        # Atualiza a validade
        self.crud.atualizar(pid, "validade", nova_validade)
        print("Validade atualizada com sucesso.")

    def ativar_inativar_produto(self):
        """
        Ativa ou inativa um produto.

        Permite alterar o status de um produto entre "ativo" e "inativo".

        :return: None
        """
        try:
            pid = int(input("ID do produto: "))
        except ValueError:
            print("ID inválido.")
            return

        # Verifica se o produto existe
        itens = self.crud.listar()
        produto = next((item for item in itens if item.get("id") == pid), None)

        if not produto:
            print("Produto não encontrado.")
            return

        status_atual = produto.get("status", "ativo")
        print(f"Status atual: {status_atual}")
        print("1 - Ativar")
        print("2 - Inativar")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            return

        if opcao == 1:
            novo_status = "ativo"
        elif opcao == 2:
            novo_status = "inativo"
        else:
            print("Opção inválida.")
            return

        # ✅ usa o método genérico agora
        self.crud.atualizar(pid, "status", novo_status)
        print(f"Produto {novo_status} com sucesso.")



