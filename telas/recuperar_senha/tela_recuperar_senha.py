import time
from utils.sistema.sistema import Sistema
from validacoes.validacoes_usuario import ValidacoesUsuario
from crud.crud import Crud

class TelaRecuperarSenha:
    def __init__(self):
        self.iniciar = True
        self.crud = Crud("jsons/dados_pessoais/usuario.json")

    def mostrar(self):
        """Esse método exibe a tela de recuperação de senha no terminal."""

        print("Informe os dados abaixo para recuperar a sua senha: \n\n")

        while self.iniciar:
            try:
                opcao = int(input("[1]- Informar os dados | [2]- voltar: "))
                if opcao not in [1, 2]:
                    Sistema.limpar_tela()
                    continue

                elif opcao == 2:
                    Sistema.limpar_tela()
                    print("Voltando..")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    return

            except ValueError:
                Sistema.limpar_tela()
                continue

            niveis = ["Funcionario", "Cliente"]

            print(f"""Informe o nível de acesso:
                    1- {niveis[0]}
                    2- {niveis[1]}
                """)

            try:
                informar_nivel = int(input("Escolha a opção correspondente ao nível do funcionário: "))
                if informar_nivel not in [1,2]:
                    print("opção inválida")
                    time.sleep(1.5)
                    Sistema.limpar_tela()
                    continue
            except ValueError:
                Sistema.limpar_tela()
                continue

            try:
                informar_cpf = input("Digite o seu cpf: ")
                ValidacoesUsuario.validar_cpf(informar_cpf)

                informar_email = input("Digite seu e-mail: ").lower()
                ValidacoesUsuario.validar_email(informar_email)
            except ValueError as erro:
                Sistema.limpar_tela()
                print(erro)
                time.sleep(1.5)
                Sistema.limpar_tela()
                continue

            if informar_nivel == 1:
                pegar_nivel = niveis[0]
            elif informar_nivel == 2:
                pegar_nivel = niveis[1]


            self._gerar_nova_senha(pegar_nivel, informar_cpf, informar_email)
            continue


    def _gerar_nova_senha(self,nivel, cpf, email):
        """Esse método abre um campo para o usuário digitar a nova senha."""

        usuario_encontrado = None

        funcionarios = Crud("jsons/dados_pessoais/usuario.json")
        clientes = Crud("jsons/dados_pessoais/solicitantes.json")

        if nivel == "Funcionario":
            for funcionario in funcionarios.listar():
                if all([funcionario.get("cpf") == cpf, funcionario.get("email") == email]):
                    usuario_encontrado = funcionario
                    break

        elif nivel == "Cliente":
            for cliente in clientes.listar():
                if all([cliente.get("cpf") == cpf, cliente.get("email") == email]):
                    usuario_encontrado = cliente
                    break



        if not usuario_encontrado:
            Sistema.limpar_tela()
            print("Usuário não encontrado")
            time.sleep(1.5)
            Sistema.limpar_tela()
            return

        while self.iniciar:
            try:
                nova_senha = input("Digite sua nova senha (4 dígitos numéricos): ")
                redigitar_senha = input("Digite novamente a nova senha: ")
                ValidacoesUsuario.validar_senha(nova_senha, redigitar_senha)
            except ValueError as erro:
                Sistema.limpar_tela()
                print(erro)
                time.sleep(1.5)
                Sistema.limpar_tela()
                continue

            self.iniciar = False
            continue

        self.iniciar = True
        if nivel == "Funcionario":
            funcionarios.atualizar(usuario_encontrado["id"], "senha", nova_senha)
        elif nivel == "Cliente":
            clientes.atualizar(usuario_encontrado["id"], "senha", nova_senha)
