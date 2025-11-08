import time
from usuarios.usuario import Cliente
from crud.crud import Crud
from utils.sistema.sistema import Sistema
from validacoes.validacoes_usuario import ValidacoesUsuario
from utils.exibir_tabela.exibir import CriarTabelas


class TelaCadastrarSolicitante:
    """
    Classe responsável pela tela de cadastro de solicitantes (clientes).

    Permite cadastrar novos solicitantes no sistema, validando os dados informados
    e verificando se o solicitante já está cadastrado antes de salvar.
    """

    def __init__(self, usuario):
        """
        Inicializa a tela de cadastro de solicitante.

        :param usuario: Dicionário com os dados do usuário responsável pelo cadastro
        """
        self.usuario = usuario
        self.json_solicitantes = "jsons/dados_pessoais/solicitantes.json"
        self.crud = Crud(self.json_solicitantes)
        self.iniciar = True

    def mostrar(self):
        """
        Exibe a tela de cadastro de solicitante no terminal.

        Solicita os dados do solicitante (nome, idade, CPF, endereço, cidade, estado,
        telefone, email, senha), valida as informações, exibe uma pré-visualização
        e permite confirmar o cadastro. Verifica se o solicitante já está cadastrado
        antes de salvar.

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
                Sistema.limpar_tela()
                continue


            cliente = Cliente(nome=nome,
                              idade=idade,
                              cpf=cpf,
                              email=email,
                              senha=senha,
                              endereco=endereco,
                              cidade=cidade,
                              estado=estado,
                              id_responsavel=self.usuario)

            Sistema.limpar_tela()

            while self.iniciar:
                print("VISUALIZAÇÃO:\n\n")
                print("Dados do cliente:\n\n")
                CriarTabelas.exibir_tabela(cliente.objeto(), titulo="Cliente")
                print("\n\n")

                condicao = input("Deseja realmente salvar esse cliente? (s/n): ").lower()

                if condicao not in ["s", "n"]:
                    Sistema.limpar_tela()
                    continue

                elif condicao == "s":
                    Sistema.limpar_tela()
                    validar = ValidacoesUsuario.validar_cadastro_usuario(self.json_solicitantes, cliente.objeto(), self.crud.listar())

                    if validar:
                        print("cliente já está cadastrado no sistema.")
                        time.sleep(1.5)
                        Sistema.limpar_tela()
                        self.iniciar = False
                        continue

                    self.crud.cadastrar(cliente.objeto())
                    print("Cliente cadastrado com sucesso")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    self.iniciar = False
                    continue
                else:
                    Sistema.limpar_tela()
                    time.sleep(1.5)
                    self.iniciar = False
                    continuec

            self.iniciar = True
            Sistema.limpar_tela()
            continue

