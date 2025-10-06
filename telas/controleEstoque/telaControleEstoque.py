import time
from crud.crud import Crud
from utils.sistema.sistema import limpar_tela
from tabulate import tabulate
from utils.alteracoes.alterar import Alteracoes
from datetime import datetime, timedelta


class TelaControleEstoque:
    def __init__(self):
        self.json_produtos = "jsons/produtos/produtos.json"
        self.crud = Crud(self.json_produtos)
        self.iniciar = True
        self.alterar = Alteracoes()

    def mostrar(self):
        while self.iniciar:
            # conta itens que vencem em 1 dia (alerta)
            try:
                alertas_um_dia = self._contar_alertas_um_dia()
            except Exception:
                alertas_um_dia = 0
            print("CONTROLE DE ESTOQUE:\n")
            print("""
                    1 - Listar estoque completo
                    2 - Filtrar por categoria
                    3 - Buscar produto por ID
                    4 - Registrar entrada (adicionar quantidade)
                    5 - Registrar saída (retirar quantidade)
                    6 - Itens com baixa de estoque
            """)
            # Imprime a opção 7 com contador dinâmico de alertas (itens que vencem amanhã)
            print(f"                    7 - Alertas de validade próxima ou vencida ({alertas_um_dia})")
            print("""
                    0 - Voltar
            """)

            try:
                opcao = int(input("Digite uma das opções acima: "))
            except ValueError:
                limpar_tela()
                continue

            if opcao == 1:
                limpar_tela()
                self.listar_estoque()
                continue
            elif opcao == 2:
                limpar_tela()
                self.filtrar_por_categoria()
                continue
            elif opcao == 3:
                limpar_tela()
                self.buscar_por_id()
                continue
            elif opcao == 4:
                limpar_tela()
                self.registrar_entrada()
                continue
            elif opcao == 5:
                limpar_tela()
                self.registrar_saida()
                continue
            elif opcao == 6:
                limpar_tela()
                self.itens_baixa_estoque()
                continue
            elif opcao == 7:
                limpar_tela()
                self.alertas_validade()
                continue
            elif opcao == 0:
                limpar_tela()
                print("Voltando...")
                time.sleep(1.2)
                limpar_tela()
                return
            else:
                limpar_tela()
                continue

    def _nome_produto(self, produto):
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
        itens = self.crud.listar()
        if not itens:
            print("Não há itens no estoque.")
            return

        linhas = []
        for item in itens:
            linhas.append([
                item.get("id"),
                item.get("categoria", ""),
                self._nome_produto(item),
                item.get("quantidade", 0),
                item.get("validade", ""),
                item.get("data_registrada", "")
            ])

        print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Qtd", "Validade", "Data"], tablefmt="fancy_grid"))

    def filtrar_por_categoria(self):
        print("1 - Medicamentos")
        print("2 - Alimentícios")
        print("3 - Vestuário")
        try:
            op = int(input("Selecione a categoria: "))
        except ValueError:
            limpar_tela()
            return

        categoria = None
        if op == 1:
            categoria = "Medicamentos"
        elif op == 2:
            categoria = "Alimentícios"
        elif op == 3:
            categoria = "Vestuário"
        else:
            limpar_tela()
            return

        itens = [i for i in self.crud.listar() if i.get("categoria") == categoria]
        if not itens:
            print(f"Nenhum item encontrado em '{categoria}'.")
            return

        linhas = []
        for item in itens:
            linhas.append([
                item.get("id"),
                item.get("categoria", ""),
                self._nome_produto(item),
                item.get("quantidade", 0),
                item.get("validade", "")
            ])
        print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Qtd", "Validade"], tablefmt="fancy_grid"))

    def buscar_por_id(self):
        try:
            pid = int(input("Informe o ID do produto: "))
        except ValueError:
            limpar_tela()
            return

        itens = self.crud.listar()
        for item in itens:
            if item.get("id") == pid:
                linhas = [[k, v] for k, v in item.items()]
                print(tabulate(linhas, headers=["Campo", "Valor"], tablefmt="fancy_grid"))
                return
        print("Produto não encontrado.")

    def registrar_entrada(self):
        try:
            pid = int(input("ID do produto: "))
            qtd = int(input("Quantidade a adicionar: "))
        except ValueError:
            limpar_tela()
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
        try:
            pid = int(input("ID do produto: "))
            qtd = int(input("Quantidade a retirar: "))
        except ValueError:
            limpar_tela()
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

    def itens_baixa_estoque(self):
        try:
            limite = int(input("Exibir itens com quantidade menor ou igual a: "))
        except ValueError:
            limpar_tela()
            return
        itens = [i for i in self.crud.listar() if i.get("quantidade", 0) <= limite]
        if not itens:
            print("Nenhum item com baixa de estoque.")
            return
        linhas = []
        for item in itens:
            linhas.append([
                item.get("id"),
                item.get("categoria", ""),
                self._nome_produto(item),
                item.get("quantidade", 0)
            ])
        print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Qtd"], tablefmt="fancy_grid"))

    def alertas_validade(self):
        # Sem entrada do usuário: usa data real e alerta de 1 dia de antecedência
        hoje = datetime.now().date()
        amanha = hoje + timedelta(days=1)

        itens = self.crud.listar()
        vencidos = []
        proximos = []

        for item in itens:
            validade_txt = item.get("validade")
            if not validade_txt:
                continue
            try:
                validade = datetime.strptime(validade_txt, "%d/%m/%Y").date()
            except Exception:
                continue

            linha = [
                item.get("id"),
                item.get("categoria", ""),
                self._nome_produto(item),
                item.get("quantidade", 0),
                validade_txt
            ]

            if validade < hoje:
                vencidos.append(linha)
            elif validade == amanha:
                proximos.append(linha)

        if not vencidos and not proximos:
            print("Nenhum item vencido ou com validade próxima no período informado.")
            return

        if vencidos:
            print("\n=== ITENS VENCIDOS ===")
            print(tabulate(vencidos, headers=["ID", "Categoria", "Produto", "Qtd", "Validade"], tablefmt="fancy_grid"))

        if proximos:
            print("\n=== ITENS COM VALIDADE PRÓXIMA ===")
            print(tabulate(proximos, headers=["ID", "Categoria", "Produto", "Qtd", "Validade"], tablefmt="fancy_grid"))

    def _contar_alertas_um_dia(self):
        """Conta quantos itens têm validade igual a amanhã (alerta de 1 dia)."""
        amanha = (datetime.now() + timedelta(days=1)).date()
        itens = self.crud.listar()
        contador = 0
        for item in itens:
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



