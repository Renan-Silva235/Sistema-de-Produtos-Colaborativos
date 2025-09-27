import time
from usuarios.usuario import Solicitante
from usuarios.gerenciador import Gerenciador
from utils.sistema.sistema import limpar_tela
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.exibir_tabela.exibir import exibir_tabela

class TelaCadastrarSolicitante:
    def __init__(self, usuario):
        self.usuario = usuario
        self.json_solicitantes = "jsons/dados_pessoais/usuario.json"
        self.gerenciador = Gerenciador(self.json_solicitantes)
        self.iniciar = True


    def mostrar(self):
        """Esse método exibe a tela de cadastro de um novo cliente(Solicitante) no terminal."""

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

            print("\n\nINFORME OS DADOS DO CLIENTE:\n\n")
            try:
                nome = input("Nome e Sobrenome: ").title()
                ValidacoesUsuario.validar_nome(nome)

                idade = int(input("Idade: "))
                ValidacoesUsuario.validar_idade(idade)

                cpf = input("CPF: ")
                ValidacoesUsuario.validar_cpf(cpf)

                endereco = input("Endereço: ")
                cidade = input("Cidade: ").title()
                estado = input("Estado: ").title()

                telefone = input("Telefone: ")
                ValidacoesUsuario.validar_telefone(telefone)

                email = input("email: ").lower()
                ValidacoesUsuario.validar_email(email)

                senha = input("Crie uma senha de 4 dígitos numéricos: ")
                redigitar_senha = input("Digite a sua senha novamente: ")
                ValidacoesUsuario.validar_senha(senha, redigitar_senha)

            except ValueError as erro:
                print(erro)
                time.sleep(1.5)
                limpar_tela()
                continue


            solicitante = Solicitante(nivel="Solicitante",
                                      nome=nome,
                                      idade=idade,
                                      cpf=cpf,
                                      email=email,
                                      senha=senha,
                                      endereco=endereco,
                                      cidade=cidade,
                                      estado=estado,
                                      id_responsavel=self.usuario["id"])

            limpar_tela()

            while self.iniciar:
                print("VISUALIZAÇÃO:\n\n")
                print("Dados do cliente:\n\n")
                exibir_tabela(solicitante.objeto(), titulo="Solicitante")
                print("\n\n")

                condicao = input("Deseja realmente salvar esse cliente? (s/n): ").lower()

                if condicao not in ["s", "n"]:
                    limpar_tela()
                    continue

                elif condicao == "s":
                    limpar_tela()
                    validar = ValidacoesUsuario.validar_cadastro_usuario(self.json_doadores, solicitante.objeto(), self.gerenciador.listar())

                    if validar:
                        print("cliente já está cadastrado no sistema.")
                        time.sleep(1.5)
                        limpar_tela()
                        self.iniciar = False
                        continue

                    self.gerenciador.cadastrar(solicitante)
                    time.sleep(1.5)
                    limpar_tela()
                    self.iniciar = False
                    continue
                else:
                    limpar_tela()
                    time.sleep(1.5)
                    self.iniciar = False
                    continue

            self.iniciar = True
            limpar_tela()
            continue

