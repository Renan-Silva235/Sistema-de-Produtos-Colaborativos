from utils.sistema.sistema import Sistema
from crud.crud import Crud
from tabulate import tabulate
from datetime import datetime
from validacoes.validacoes_produtos import ValidacoesProdutos
import time


class TelaRelatorio:
    """
    Classe responsável pela tela de relatórios do sistema.

    Fornece diversos relatórios sobre produtos, doações, categorias e estatísticas
    do sistema, incluindo produtos mais pedidos, doações por período e por doador.
    """

    def __init__(self):
        """
        Inicializa a tela de relatórios.
        """
        self.produtosEstoque = Crud("jsons/produtos/produtos.json")
        self.doadoresCrud = Crud("jsons/dados_pessoais/doadores.json")

    def mostrar(self):
        """
        Exibe o menu principal de relatórios no terminal.

        Apresenta estatísticas gerais e opções para visualizar relatórios detalhados:
        - Visualizar tabelas por categoria
        - Relatório de doações por período
        - Relatório de doações por doador

        :return: None
        """
        while True:
            print("======= Relatórios =======\n")
            self.produtosMaisPedidos()
            print("\n")
            self.quantidadeProdutosCategoria()
            print("\n")
            self.totalProdutosDoados()
            print("\n")
            print("1 - Visualizar Tabelas por Categoria")
            print("2 - Relatório de doações por período")
            print("3 - Relatório de doações por doador")
            try:
                verCategoria = int(input("Digite uma das opções acima ou 0 para sair: "))
                Sistema.limpar_tela()
                if verCategoria == 1:
                    Sistema.limpar_tela()
                    self.visualizarProdutosPorCategoria()
                elif verCategoria == 2:
                    Sistema.limpar_tela()
                    self.relatorioDoacoesPorPeriodo()
                elif verCategoria == 3:
                    Sistema.limpar_tela()
                    self.relatorioDoacoesPorDoador()
                elif verCategoria == 0:
                    Sistema.limpar_tela()
                    return
                else:
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue
            print("\n==========================")



    def quantidadeProdutosCategoria(self):
        """
        Exibe a quantidade de produtos por categoria.

        Conta quantos produtos existem em cada categoria (Medicamentos, Alimentícios, Vestuário)
        e exibe o total de produtos cadastrados.

        :return: None
        """
        produtos = self.produtosEstoque.listar()
        categorias = {}
        for produto in produtos:
            categoria = produto['categoria']
            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1
        tabela = [[categoria, quantidade] for categoria, quantidade in categorias.items()]
        tabela.append(["Total de produtos cadastrados", len(produtos)])
        print(tabulate(tabela, headers=["Categoria", "Quantidade"], tablefmt="fancy_grid"))



    def tabelaProdutosPorCategoria(self, categoria=None):
        """
        Exibe uma tabela com todos os produtos de uma categoria específica.

        :param categoria: String com o nome da categoria (Medicamentos, Alimentícios ou Vestuário)
        :return: None
        """
        produtos_categoria = [item for item in self.produtosEstoque.listar() if item.get('categoria') == categoria]
        if not produtos_categoria:
            print(f"Nenhum produto encontrado na categoria '{categoria}'.")
            return

        # Usa as chaves do primeiro produto como cabeçalho
        colunas = list(produtos_categoria[0].keys())
        tabela = [[produto.get(coluna, '') for coluna in colunas] for produto in produtos_categoria]

        print(f"\nProdutos da categoria: {categoria}")
        print(tabulate(tabela, headers=colunas, tablefmt="fancy_grid"))

    def visualizarProdutosPorCategoria(self):
        """
        Permite visualizar produtos filtrados por categoria.

        Solicita a categoria desejada e exibe todos os produtos dessa categoria.

        :return: None
        """
        while True:
            print("1 - Medicamentos")
            print("2 - Alimentícios")
            print("3 - Vestuário")
            print("0 - Voltar\n\n")


            try:
                opcao = int(input("Selecione a categoria ou 0 para voltar: "))
                if opcao == 1:
                    self.tabelaProdutosPorCategoria("Medicamentos")
                elif opcao == 2:
                    self.tabelaProdutosPorCategoria("Alimentícios")
                elif opcao == 3:
                    self.tabelaProdutosPorCategoria("Vestuário")
                elif opcao == 0:
                    Sistema.limpar_tela()
                    return
                else:
                    Sistema.limpar_tela()
                    continue

            except ValueError:
                Sistema.limpar_tela()
                continue


    def totalProdutosDoados(self):
        """
        Calcula e exibe o total de produtos doados.

        Soma todas as quantidades pedidas de produtos aprovados para doação.

        :return: None
        """

        contador = 0

        pedidos_aprovados = Crud("jsons/solicitacoes/aprovados.json")

        for pedido in pedidos_aprovados.listar():
            for produto in pedido.get("pedido", []):

                contador += produto.get("quantidade_pedida", 0)

        tabela = [["Total de Produtos Doados", contador]]
        print(tabulate(tabela, tablefmt="fancy_grid"))

    def produtosMaisPedidos(self):
        """
        Analisa os pedidos aprovados e reprovados e exibe um ranking dos produtos mais pedidos pelos solicitantes.
        Conta quantas vezes cada ID de produto aparece nos pedidos.
        """
        pedidos_aprovados = Crud("jsons/solicitacoes/aprovados.json")
        pedidos_reprovados = Crud("jsons/solicitacoes/reprovados.json")
        id_contagem = {}

        # Conta quantas vezes cada ID de produto aparece nos pedidos aprovados
        for pedido in pedidos_aprovados.listar():
            for produto in pedido.get("pedido", []):
                produto_id = produto.get("id", "")

                if produto_id in id_contagem:
                    id_contagem[produto_id] += 1
                else:
                    id_contagem[produto_id] = 1

        # Conta quantas vezes cada ID de produto aparece nos pedidos reprovados
        for pedido in pedidos_reprovados.listar():
            for produto in pedido.get("pedido", []):
                produto_id = produto.get("id", "")

                if produto_id in id_contagem:
                    id_contagem[produto_id] += 1
                else:
                    id_contagem[produto_id] = 1

        if not id_contagem:
            print("Nenhum produto foi pedido ainda.")
            return

        # Ordena os IDs por frequência (maior para menor)
        ids_ordenados = sorted(id_contagem.items(), key=lambda x: x[1], reverse=True)

        # Busca os nomes dos produtos no estoque
        produtos_estoque = self.produtosEstoque.listar()

        # Cria a tabela com os IDs mais pedidos e seus nomes
        tabela = []
        for i, (produto_id, frequencia) in enumerate(ids_ordenados, 1):
            # Busca o nome do produto no estoque
            nome_produto = "Produto não encontrado"
            for produto in produtos_estoque:
                if produto.get("id") == produto_id:
                    categoria = produto.get("categoria", "")
                    # Determina o nome do produto baseado na categoria
                    if categoria == "Medicamentos":
                        nome_produto = produto.get("nome_medicamento", ["Produto sem nome"])[0] if isinstance(produto.get("nome_medicamento"), list) else produto.get("nome_medicamento", "Produto sem nome")
                    elif categoria == "Alimentícios":
                        nome_produto = produto.get("nome_alimento", "Produto sem nome")
                    elif categoria == "Vestuário":
                        nome_produto = produto.get("nome_produto", "Produto sem nome")
                    break

            tabela.append([i, produto_id, nome_produto, frequencia])

        print("\n=== RANKING DOS PRODUTOS MAIS PEDIDOS ===")
        print(tabulate(tabela, headers=["Posição", "ID", "Nome do Produto", "Total de Solicitações"], tablefmt="fancy_grid"))




    def formato_data(self, texto):
        """
        Converte uma string de data no formato dd/mm/aaaa para objeto datetime.

        :param texto: String com a data no formato dd/mm/aaaa
        :return: Objeto datetime se a conversão for bem-sucedida, None caso contrário
        """
        try:
            return datetime.strptime(texto.strip(), "%d/%m/%Y")
        except Exception:
            return None

    def _parse_data_ddmmyyyy(self, texto):
        """
        Compatibilidade: retorna um datetime a partir de string dd/mm/aaaa
        ou None em caso de formato inválido.
        """
        return self.formato_data(texto)

    def _nome_produto(self, produto):
        """
        Retorna o nome do produto baseado na sua categoria.

        :param produto: Dicionário com os dados do produto
        :return: String com o nome do produto ou "Produto sem nome" se não encontrado
        """
        categoria = produto.get("categoria", "")
        if categoria == "Medicamentos":
            valor = produto.get("nome_medicamento")
            return valor[0] if isinstance(valor, list) and valor else (valor or "Produto sem nome")
        if categoria == "Alimentícios":
            return produto.get("nome_alimento", "Produto sem nome")
        if categoria == "Vestuário":
            return produto.get("nome_produto", "Produto sem nome")
        return "Produto sem nome"

    def relatorioDoacoesPorPeriodo(self):
        """
        Gera relatório de doações por período.

        Solicita uma data inicial e final, e exibe todas as doações registradas
        nesse período, incluindo o total de itens doados.

        :return: None
        """
        while True:
            print("=== RELATÓRIO DE DOAÇÕES POR PERÍODO ===")
            print("Informe as datas no formato dd/mm/aaaa")
            try:
                inicio_txt = input("Data inicial: ")
                ValidacoesProdutos.validar_formato_data(inicio_txt)
                fim_txt = input("Data final:   ")
                ValidacoesProdutos.validar_formato_data(fim_txt)
            except ValueError as error:
                Sistema.limpar_tela()
                print(error)
                time.sleep(1.5)
                Sistema.limpar_tela()
                continue


            dt_inicio = self._parse_data_ddmmyyyy(inicio_txt)
            dt_fim = self._parse_data_ddmmyyyy(fim_txt)

            if not dt_inicio or not dt_fim or dt_fim < dt_inicio:
                print("Período inválido. Use dd/mm/aaaa e verifique se a data final não é menor que a inicial.")
                return

            # Ajusta para início e fim do dia
            dt_inicio = datetime(dt_inicio.year, dt_inicio.month, dt_inicio.day, 0, 0, 0)
            dt_fim = datetime(dt_fim.year, dt_fim.month, dt_fim.day, 23, 59, 59)

            itens = self.produtosEstoque.listar()
            if not itens:
                print("Não há doações registradas.")
                return

            linhas = []
            total_quantidade = 0

            for item in itens:
                data_txt = item.get("data_registrada")
                if not data_txt:
                    continue
                try:
                    dt_item = datetime.strptime(data_txt, "%d/%m/%Y %H:%M:%S")
                except Exception:
                    continue

                if dt_inicio <= dt_item <= dt_fim:
                    nome = self._nome_produto(item)
                    linhas.append([
                        item.get("id"),
                        item.get("categoria", ""),
                        nome,
                        item.get("quantidade", 0),
                        data_txt
                    ])
                    total_quantidade += item.get("quantidade", 0)

            if not linhas:
                print("Nenhuma doação encontrada no período informado.")
                return

            print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Quantidade", "Data Registrada"], tablefmt="fancy_grid"))
            print(tabulate([["Total de itens doados no período", total_quantidade]], tablefmt="fancy_grid"))
            input("tecle enter para voltar")
            Sistema.limpar_tela()
            return

    def relatorioDoacoesPorDoador(self):
        """
        Gera relatório de doações por doador.

        Solicita o nome ou CPF do doador e exibe todas as doações realizadas por ele,
        incluindo o total de itens doados.

        :return: None
        """
        print("=== RELATÓRIO DE DOAÇÕES POR DOADOR ===")
        chave = input("Informe o nome ou CPF do doador: ").strip()

        doadores = self.doadoresCrud.listar()
        if not doadores:
            print("Não há doadores cadastrados.")
            return

        doador_encontrado = None
        for d in doadores:
            if str(d.get("cpf", "")).strip() == chave or str(d.get("nome", "")).strip().lower() == chave.lower():
                doador_encontrado = d
                break

        if not doador_encontrado:
            print("Doador não encontrado. Pesquise pelo nome exato ou CPF.")
            return

        doador_id = doador_encontrado.get("id")
        itens = self.produtosEstoque.listar()
        if not itens:
            print("Não há doações registradas.")
            return

        linhas = []
        total_quantidade = 0

        for item in itens:
            ids_doadores = item.get("id_doador", []) or []
            if doador_id in ids_doadores:
                nome = self._nome_produto(item)
                linhas.append([
                    item.get("id"),
                    item.get("categoria", ""),
                    nome,
                    item.get("quantidade", 0),
                    item.get("data_registrada", "")
                ])
                total_quantidade += item.get("quantidade", 0)

        if not linhas:
            print("Esse doador ainda não possui doações registradas.")
            return

        titulo = f"Doações do doador: {doador_encontrado.get('nome')} (CPF: {doador_encontrado.get('cpf')})"
        print(titulo)
        print(tabulate(linhas, headers=["ID", "Categoria", "Produto", "Quantidade", "Data Registrada"], tablefmt="fancy_grid"))
        print(tabulate([["Total de itens doados (todas as entradas)", total_quantidade]], tablefmt="fancy_grid"))
        input("Tecle enter para voltar")
        Sistema.limpar_tela()
        return

