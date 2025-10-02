import time
from utils.sistema.sistema import limpar_tela
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
                    limpar_tela()
                    continue

                elif opcao == 2:
                    limpar_tela()
                    print("Voltando..")
                    time.sleep(1.5)
                    limpar_tela()
                    return

            except ValueError:
                limpar_tela()
                continue

            niveis = ["Administrador", "Voluntário", "Solicitante"]

            print(f"""Informe o nível de acesso:
                    1- {niveis[0]}
                    2- {niveis[1]}
                    3- {niveis[2]}
                """)

            try:
                informar_nivel = int(input("Escolha a opção correspondente ao nível do funcionário: "))
                if informar_nivel not in [1,2,3]:
                    print("opção inválida")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
            except ValueError:
                limpar_tela()
                continue

            try:
                informar_cpf = input("Digite o seu cpf: ")
                ValidacoesUsuario.validar_cpf(informar_cpf)

                informar_email = input("Digite seu e-mail: ").lower()
                ValidacoesUsuario.validar_email(informar_email)
            except ValueError as erro:
                limpar_tela()
                print(erro)
                time.sleep(1.5)
                limpar_tela()
                continue

            if informar_nivel == 1:
                pegar_nivel = niveis[0]
            elif informar_nivel == 2:
                pegar_nivel = niveis[1]
            else:
                pegar_nivel = niveis[2]

            self._gerar_nova_senha(pegar_nivel, informar_cpf, informar_email)
            continue


    def _gerar_nova_senha(self,nivel, cpf, email):
        """Esse método abre um campo para o usuário digitar a nova senha."""

        usuario_encontrado = None

        consultar = self.crud.listar()


        for usuario in consultar:
            if all([usuario.get("nivel") == nivel, usuario.get("cpf") == cpf, usuario.get("email") == email]):
                usuario_encontrado = usuario
                break

        if not usuario_encontrado:
            print("Usuário não encontrado")
            return False

        while self.iniciar:
            try:
                nova_senha = input("Digite sua nova senha (4 dígitos numéricos): ")
                redigitar_senha = input("Digite novamente a nova senha: ")
                ValidacoesUsuario.validar_senha(nova_senha, redigitar_senha)
            except ValueError as erro:
                limpar_tela()
                print(erro)
                time.sleep(1.5)
                limpar_tela()
                continue

            self.iniciar = False
            continue

        self.iniciar = True
        self.crud.atualizar("senha", usuario_encontrado["senha"], nova_senha)
        print("Senha alterada com sucesso!")
        return
