import re


class ValidacoesUsuario:
    """
    Classe responsável por validar dados de usuários.

    Contém métodos estáticos para validar nome, idade, CPF, email, senha, telefone
    e verificar se um usuário já está cadastrado no sistema.
    """

    @staticmethod
    def validar_nome(nome):
        """
        Valida se o nome contém apenas letras (com acentos) e espaços.

        :param nome: String com o nome a ser validado
        :return: True se o nome for válido
        :raises ValueError: Se o nome for None, vazio, menor que 2 caracteres
                           ou contiver símbolos/números
        """
        if nome is None:
            raise ValueError("Campo nome está vazio")

        if nome == "":
            raise ValueError("Campo 'nome' não pode estar vazio")

        nome = nome.strip()
        if len(nome) < 2:
            raise ValueError("Nome Inválido")

        # Regex: apenas letras (com acentos) e espaços
        if not re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome):
            raise ValueError("Nome Inválido: utilize apenas letras")

        return True

    @staticmethod
    def validar_idade(idade):
        """
        Valida se a idade é um número inteiro não negativo.

        :param idade: Inteiro representando a idade
        :return: True se a idade for válida
        :raises ValueError: Se a idade não for um inteiro ou for negativa
        """
        if type(idade) != int:
            raise ValueError("Idade Inválida")

        if idade < 0:
            raise ValueError("Idade Inválida")
        return True


    @staticmethod
    def validar_cpf(cpf):
        """
        Valida se o CPF está no formato correto (11 dígitos numéricos).

        :param cpf: String com o CPF a ser validado
        :return: True se o CPF estiver no formato correto
        :raises ValueError: Se o CPF não for uma string, não contiver apenas dígitos
                           ou não tiver exatamente 11 caracteres
        """
        if not isinstance(cpf, str):
            raise ValueError("CPF Inválido")

        cpf = cpf.strip()

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF Inválido")

        return True

    @staticmethod
    def validar_email(email):
        """
        Valida se o email está em um formato básico válido.

        Verifica se contém '@' e '.' após o '@'.

        :param email: String com o email a ser validado
        :return: True se o email estiver no formato válido
        :raises ValueError: Se o email estiver vazio ou em formato inválido
        """
        if not email:
            raise ValueError("E-mail vazio")

        if "@" not in email or "." not in email:
            raise ValueError("E-mail inválido")

        # garante que o ponto vem depois do @
        index_arroba = email.index("@")
        if "." not in email[index_arroba:]:
            raise ValueError("E-mail inválido")

        return True

    @staticmethod
    def validar_senha(senha, redigitar_senha=None):
        """
        Valida se a senha está no formato correto (4 dígitos numéricos).

        :param senha: String com a senha a ser validada
        :param redigitar_senha: Opcional. String com a confirmação da senha
        :return: True se a senha for válida e, se fornecido, igual à confirmação
        :raises ValueError: Se a senha estiver vazia, não contiver apenas dígitos,
                           não tiver 4 caracteres ou não coincidir com a confirmação
        """
        if senha == "":
            raise ValueError("campo senha é obrigatório")

        if not senha.isdigit():
            raise ValueError("Senha Inválida")

        if len(senha) != 4:
            raise ValueError("Senha deve conter apenas números e deve conter 4 dígitos.")

        if redigitar_senha is not None:
            if redigitar_senha != senha:
                raise ValueError("Senhas não coincidem")

        return True

    @staticmethod
    def validar_telefone(telefone):
        """
        Valida se o telefone está no formato correto (apenas números, entre 8 e 15 dígitos).

        :param telefone: String com o telefone a ser validado
        :return: True se o telefone for válido
        :raises ValueError: Se o telefone não contiver apenas dígitos ou
                           não tiver entre 8 e 15 caracteres
        """
        telefone = telefone.strip()  # remove espaços no começo/fim

        if not telefone.isdigit():
            raise ValueError("Telefone inválido: deve conter apenas números")

        if not (8 <= len(telefone) <= 15):
            raise ValueError("Telefone inválido: deve ter entre 8 e 15 dígitos")

        return True


    @staticmethod
    def validar_cadastro_usuario(caminho_arquivo, objeto, consulta):
        """
        Verifica se o usuário já está cadastrado no sistema baseado no CPF.

        Compara os campos do objeto fornecido com os dados na lista de consulta.
        Suporta verificação em doadores, usuários e solicitantes.

        :param caminho_arquivo: String com o caminho do arquivo JSON (doadores.json,
                               usuario.json ou solicitantes.json)
        :param objeto: Dicionário com os dados do usuário a ser verificado (deve conter 'cpf')
        :param consulta: Lista de dicionários com os dados já cadastrados no sistema
        :return: True se o usuário já estiver cadastrado, False caso contrário
        """
        regras = {
            "jsons/dados_pessoais/doadores.json": ["cpf"],
            "jsons/dados_pessoais/usuario.json": ["cpf"],
            "jsons/dados_pessoais/solicitantes.json": ["cpf"],
        }

        campos = regras.get(caminho_arquivo)
        if not campos:
            return False

        for consultado in consulta:
            if all(consultado.get(campo) == objeto.get(campo) for campo in campos):
                return True

        return False

