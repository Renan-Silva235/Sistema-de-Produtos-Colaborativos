import re


class ValidacoesUsuario:

    @staticmethod
    def validar_nome(nome):
        """
        Retorna True se o nome for válido:
        - Apenas letras, acentos, hífen e apóstrofo
        - Pelo menos 2 caracteres
        """
        if nome is None:
            raise ValueError("Campo nome está vazio")

        if nome == "":
            raise ValueError("Campo 'nome' não pode estar vazio")

        nome = nome.strip()
        if len(nome) < 2:
            raise ValueError("Nome Inválido")

        # Regex: letras + acentos + hífen + apóstrofo
        return bool(re.fullmatch(r"[A-Za-zÀ-ÿ'-]+", nome))

    @staticmethod
    def validar_idade(idade):
        """Valida idade (apenas inteiros)."""
        if not isinstance(idade, int) or idade < 0:
            raise ValueError("Idade Inválida")
        return True


    @staticmethod
    def validar_cpf(cpf):
        """Valida formato de CPF (apenas tamanho e dígitos)."""
        if not cpf.isdigit() and len(cpf) != 11:
            raise ValueError("CPF Inválido")

        return True

    @staticmethod
    def validar_email(email):
        """Valida formato básico de email."""
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
        """Validar formato básico da senha"""
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
        Valida telefone:
        - Apenas números
        - Entre 8 e 15 dígitos
        """
        telefone = telefone.strip()  # remove espaços no começo/fim

        if not telefone.isdigit():
            raise ValueError("Telefone inválido: deve conter apenas números")

        if not (8 <= len(telefone) <= 15):
            raise ValueError("Telefone inválido: deve ter entre 8 e 15 dígitos")

        return True


    @staticmethod
    def validar_cadastro_usuario(caminho_arquivo, objeto, consulta):
        """Valida se o produto já está cadastrado na categoria correspondente."""

        regras = {
            "jsons/dados_pessoais/doadores.json": ["cpf"],
            "jsons/dados_pessoais/usuario.json": ["cpf"]
        }

        campos = regras.get(caminho_arquivo)
        if not campos:
            return False

        for consultado in consulta:
            if all(consultado.get(campo) == objeto.get(campo) for campo in campos):
                return True

        return False

