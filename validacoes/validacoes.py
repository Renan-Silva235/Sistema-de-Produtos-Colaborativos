import json
import re
from datetime import datetime


class Validacoes:


    def validar_login(self, nivel, usuario, senha):
        """Esse método Valida todos os dados de login que o usuário digitar, verificando
        cada tipo, tamanho e permissão. Se retornar 'True' o usuário será direcionado para a tela
        correspondente ao seu nível na empresa"""

        arquivo = None
        nivel_usuario = None
        logado = False

        if nivel == 1:
            arquivo = "json/dados_pessoais/dados_funcionarios.json"
            nivel_usuario = "Administrador"
        elif nivel == 2:
            arquivo = "json/dados_pessoais/dados_funcionarios.json"
            nivel_usuario = "Voluntário"
        else:
            arquivo = "json/dados_pessoais/dados_solicitantes.json"
            nivel_usuario = "Solicitante"

        with open(arquivo, "r", encoding="utf-8") as arq:
            usuarios = json.load(arq)

        for user in usuarios:
            if nivel_usuario == "Solicitante":
                if user.get("email") == usuario and user.get("senha") == senha:
                    logado = True
                    return logado
            elif user.get("nivel") == nivel_usuario and user.get("emailCorporativo") == usuario and user.get("senha") == senha:
                logado = True
                return logado


        return logado


    @staticmethod
    def validar_cpf(cpf):
        """Valida formato de CPF (apenas tamanho e dígitos)."""
        return cpf.isdigit() and len(cpf) == 11

    @staticmethod
    def validar_email(email):
        """Valida formato básico de email."""
        return "@" in email and "." in email and email != ""

    @staticmethod
    def validar_senha(senha):
        """Validar formato básico da senha"""
        return senha.isdigit() and len(senha) == 4 and senha != ""

    @staticmethod
    def validar_formato_data(data):
        """Valida se a string de data está no formato esperado (dd/mm/yy)."""
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def validar_peso(peso: str) -> bool:
        """
        Retorna True apenas se `peso` tiver o formato:
          <número> [espaço opcional] <unidade>
        onde unidade é uma de: g, kg, l, ml (qualquer caixa).
        O número pode ter decimal com '.' ou ','.
        Exemplos válidos: "500G", "0.5 kg", "250 ml", "1,25Kg"
        Exemplos inválidos: "G500", "4 Gg", "abcKg", "123" (sem unidade)
        """
        if not isinstance(peso, str):
            return False

        s = peso.strip()
        # ^...$ garante que toda a string deve casar (sem sobras)
        pattern = re.compile(r'^([+-]?\d+(?:[.,]\d+)?)\s*(kg|g|ml|l)$', re.IGNORECASE)
        m = pattern.fullmatch(s)
        if not m:
            return False

        num_str = m.group(1).replace(',', '.')
        try:
            num = float(num_str)
        except ValueError:
            return False

        return num > 0
