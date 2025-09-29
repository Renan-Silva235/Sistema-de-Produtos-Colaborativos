import time
from utils.sistema.sistema import limpar_tela
from utils.exibir_tabela.exibir import exibir_tabela
from usuarios.gerenciador import Gerenciador
from validacoes.validacoes_usuario import ValidacoesUsuario
from usuarios.doadores import Doador

class TelaCadastrarDoador:
    def __init__(self, usuario):
        self.json_doadores = "jsons/dados_pessoais/doadores.json"
        self.gerenciador = Gerenciador(self.json_doadores)
        self.iniciar = True
        self.usuario = usuario

    def mostrar(self):
        """Esse método exibe a tela de cadastro de produtos no terminal."""

        while self.iniciar:
            try:
                continuar_ou_não = int(input("[1]- Informar os dados | [2]- voltar: "))
                if continuar_ou_não not in [1, 2]:
                    limpar_tela()
                    continue

                elif continuar_ou_não == 2:
                    limpar_tela()
                    print("Voltando..")
                    time.sleep(1.5)
                    limpar_tela()
                    return

            except ValueError:
                limpar_tela()
                continue

            print("\n\nINFORME OS DADOS DO DOADOR:\n\n")
            try:
                nome = input("Digite seu nome: ").title()
                ValidacoesUsuario.validar_nome(nome)

                idade = int(input("Digite sua idade: "))
                ValidacoesUsuario.validar_idade(idade)

                cpf = input("Digite o seu CPF: ")
                ValidacoesUsuario.validar_cpf(cpf)

                cidade = input("Digite a sua cidade: ").title()
                estado = input("Digite o seu estado: ").title()

                email = input("Digite seu email: ").lower()
                ValidacoesUsuario.validar_email(email)

                telefone = input("Digite o seu telefone: ")
                ValidacoesUsuario.validar_telefone(telefone)

            except ValueError as erro:
                limpar_tela()
                print(erro)
                time.sleep(1.5)
                limpar_tela()
                continue

            doador = Doador(nome=nome, idade=idade, cpf=cpf, telefone=telefone, email=email, cidade=cidade, estado=estado, id_responsavel=self.usuario["id"])

            limpar_tela()

            confirmar = True
            while confirmar:
                print("VISUALIZAÇÃO:\n\n")
                print("Dados do Doador:\n\n")
                exibir_tabela(doador.objeto(), titulo="Doador")
                print("\n\n")

                condicao = input("Deseja realmente salvar esse doador? (s/n): ").lower()

                if condicao not in ["s", "n"]:
                    limpar_tela()
                    continue

                elif condicao == "s":
                    limpar_tela()
                    consultar = self.gerenciador.listar()
                    validar = ValidacoesUsuario.validar_cadastro_usuario(self.json_doadores, doador.objeto(), consultar)

                    if validar:
                        print("Doador já está cadastrado no sistema.")
                        time.sleep(1.5)
                        limpar_tela()
                        confirmar = False
                        continue

                    self.gerenciador.cadastrar(doador.objeto())
                    print("Doador Cadastrado com sucesso")
                    time.sleep(1.5)
                    limpar_tela()
                    confirmar = False
                    continue
                else:
                    limpar_tela()
                    time.sleep(1.5)
                    confirmar = False
                    continue

            limpar_tela()
