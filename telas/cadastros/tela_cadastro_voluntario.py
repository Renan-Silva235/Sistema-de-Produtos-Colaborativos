import time
from utils.exibir_tabela.exibir import exibir_tabela
from usuarios.usuario import Usuario
from crud.crud import Crud
from utils.sistema.sistema import limpar_tela
from validacoes.validacoes_usuario import ValidacoesUsuario

class TelaCadastrarVoluntario:
    def __init__(self, usuario):
        self.usuario = usuario
        self.json_voluntario = "jsons/dados_pessoais/usuario.json"
        self.crud = Crud(self.json_voluntario)
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

            niveis = ["Administrador", "Voluntário"]

            print(f"""Informe o nível do funcionário:
                    1- {niveis[0]}
                    2- {niveis[1]}
                """)

            try:
                opcao_nivel = int(input("Escolha a opção correspondente ao nível do funcionário: "))
                if opcao_nivel not in [1,2]:
                    print("opção inválida")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
            except ValueError:
                limpar_tela()
                continue

            print("\n\nINFORME OS DADOS DO NOVO FUNCIONÁRIO:\n\n")
            try:
                nome = input("Nome: ").title()
                ValidacoesUsuario.validar_nome(nome)

                idade = int(input("Idade: "))
                ValidacoesUsuario.validar_idade(idade)

                cpf = input("CPF: ")
                ValidacoesUsuario.validar_cpf(cpf)

                email = input("email: ").lower()
                ValidacoesUsuario.validar_email(email)

                senha = input("Crie uma senha de 4 dígitos numérica: ")
                redigitar_senha = input("Digite a sua senha novamente: ")
                ValidacoesUsuario.validar_senha(senha, redigitar_senha)


            except ValueError as erro:
                print(erro)
                time.sleep(1.5)
                limpar_tela()
                continue

            if opcao_nivel == 1:
                nivel_funcionario = niveis[0]
            else:
                nivel_funcionario = niveis[1]

            usuario = Usuario(nivel=nivel_funcionario, nome=nome, idade=idade, cpf=cpf, email=email, senha=senha)


            limpar_tela()

            while self.iniciar:
                print("VISUALIZAÇÃO:\n\n")
                print("Dados do funcionário:\n\n")
                exibir_tabela(usuario.objeto(), titulo="Voluntário")
                print("\n\n")

                condicao = input("Deseja realmente salvar esse cliente? (s/n): ").lower()

                if condicao not in ["s", "n"]:
                    limpar_tela()
                    continue

                elif condicao == "s":
                    limpar_tela()
                    validar = ValidacoesUsuario.validar_cadastro_usuario(self.json_voluntario, usuario.objeto(), self.gerenciador.listar())

                    if validar:
                        print("Funcionário já está cadastrado no sistema.")
                        time.sleep(1.5)
                        limpar_tela()
                        self.iniciar = False
                        continue

                    self.gerenciador.cadastrar(usuario.objeto())
                    print("Funcionário cadastrado com sucesso.")
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
