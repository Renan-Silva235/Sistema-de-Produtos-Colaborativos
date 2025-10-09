import time
from utils.sistema.sistema import Sistema
from telas.cadastros.tela_cadastro_produtos import TelaCadastrarProdutos
from telas.cadastros.tela_cadastro_doador import TelaCadastrarDoador
from telas.cadastros.tela_cadastro_Solicitante import TelaCadastrarSolicitante
from telas.cadastros.tela_cadastro_voluntario import TelaCadastrarVoluntario

class TelaMenuCadastro:

    def __init__(self, usuario):
        self.usuario = usuario
        self.iniciar = True

    def mostrar(self):
        """Esse método exibe um menu com diferentes tipos de cadastros que o admin
         pode fazer no terminal."""


        while self.iniciar:
            print("""Digite o número relacionado ao que você quer cadastrar:\n""")
            print("""
                        1- Cadastrar Produto
                        2- Cadastrar Doador
                        3- Cadastrar Solicitante
                        4- Cadastrar Voluntário
                        0- Voltar
                    \n""")

            try:
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    Sistema.limpar_tela()
                    self.telaCadastroProduto = TelaCadastrarProdutos(self.usuario)
                    self.telaCadastroProduto.mostrar()
                    continue
                elif opcao == 2:
                    Sistema.limpar_tela()
                    self.telaCadastroDoador = TelaCadastrarDoador(self.usuario)
                    self.telaCadastroDoador.mostrar()
                    continue
                elif opcao == 3:
                    Sistema.limpar_tela()
                    self.telaCadastroSolicitante = TelaCadastrarSolicitante(self.usuario)
                    self.telaCadastroSolicitante.mostrar()
                    continue
                elif opcao == 4:
                    Sistema.limpar_tela()
                    self.telaCadastroVoluntario = TelaCadastrarVoluntario(self.usuario)
                    self.telaCadastroVoluntario.mostrar()
                    continue
                elif opcao == 0:
                    Sistema.limpar_tela()
                    print("Voltando para tela de Admin...")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return
                else:
                    Sistema.limpar_tela()
                    print("Opção Inválida")
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue

