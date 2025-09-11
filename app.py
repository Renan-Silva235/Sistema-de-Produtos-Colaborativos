from telas.gerenciadorTelas.gerenciador_telas import GerenciadorTelas

def RodarPrograma():
    """Essa é a função main do programa, onde o software começa a rodar"""
    gerenciador = GerenciadorTelas()
    gerenciador.iniciar("TelaCadastrarProdutos")


if __name__ == "__main__":
    RodarPrograma()
