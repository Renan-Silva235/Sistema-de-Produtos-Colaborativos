from utils.sistema.sistema import limpar_tela
from crud.crud import Crud
from tabulate import tabulate

class TelaRelatorio:
    def __init__(self):
        self.produtosEstoque = Crud("jsons/produtos/produtos.json")
        
    def mostrar(self):
        while True:
            print("======= Relatórios =======\n")
            self.produtosMaisPedidos()
            print("\n")
            self.quantidadeProdutosCategoria()  
            print("\n")
            self.totalProdutosDoados()
            print("\n")
            print("1 - Visualizar Tabelas por Categoria")
            try:
                verCategoria = int(input("Digite uma das opções acima ou 0 para sair: "))
                limpar_tela()
                if verCategoria == 1:
                    self.visualizarProdutosPorCategoria()
                elif verCategoria == 0:
                    limpar_tela()
                    return
                else:
                    limpar_tela()
                    continue
            except ValueError:
                limpar_tela()
                continue
        print("\n==========================")

        

    def quantidadeProdutosCategoria(self):
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
                    limpar_tela()
                    return
                else:
                    limpar_tela()
                    continue

            except ValueError:
                limpar_tela()
                continue


    def totalProdutosDoados(self):

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
        
        


# p1 = TelaRelatorio()
# p1.mostrar()