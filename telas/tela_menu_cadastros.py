import time
from utils.sistema import limpar_tela

class TelaMenuCadastro:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def mostrar(self):

        print("""Digite o número relacionado ao que você quer cadastrar:""")
        print("""
                    1- Cadastrar Produto
                    2- Cadastrar Doador
                    3- Cadastrar Solicitante
                    4- Cadastrar Voluntário
                    0- Voltar a tela de Administração
                """)

        while True:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                limpar_tela()
                self.gerenciador.mudar_tela("TelaCadastrarProdutos")
                break
            elif opcao == 2:
                print("Cadastrar Doador")
                break
            elif opcao == 3:
                print("Cadastrar Solicitante ")
                break
            elif opcao == 4:
                print("Cadastrar Voluntário")
                break
            elif opcao == 0:
                limpar_tela()
                print("Voltando a tela de Admin...")
                time.sleep(2)
                limpar_tela()
                self.gerenciador.mudar_tela("TelaAdministrador")
                limpar_tela()
                break
            else:
                limpar_tela()
                print("Opção Inválida")
                limpar_tela()
                continue



