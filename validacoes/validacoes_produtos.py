import re
from datetime import datetime


class ValidacoesProdutos:

    @staticmethod
    def validar_cadastro_produto(caminho_arquivo, objeto, consulta):
        """Valida se o produto já está cadastrado na categoria correspondente."""

        regras = {
            "jsons/categorias/alimentos.json": ["nome_alimento", "peso", "validade"],
            "jsons/categorias/medicamentos.json": ["nome_comercial", "nome_generico", "categoria", "dosagem", "validade"],
            "jsons/categorias/vestuario.json": ["nome_produto", "cor", "marca", "tamanho"],
        }

        campos = regras.get(caminho_arquivo)
        if not campos:
            return False

        for consultado in consulta:
            if all(consultado.get(campo) == objeto.get(campo) for campo in campos):
                return consultado["id"]

        return False


    @staticmethod
    def validar_formato_data(data):
        """Valida se a string de data está no formato esperado (dd/mm/yyyy)."""
        try:
            datetime.strptime(data, "%d/%m/%Y")  # tenta converter
            return True
        except ValueError:
            raise ValueError("Formato de data inválido. Use dd/mm/aaaa")

    @staticmethod
    def validar_peso(peso):
        """
        Retorna True apenas se `peso` tiver o formato:
          <número> [espaço opcional] <unidade>
        onde unidade é uma de: g, kg, l, ml (qualquer caixa).
        O número pode ter decimal com '.' ou ','.
        Exemplos válidos: "500G", "0.5 kg", "250 ml", "1,25Kg"
        Exemplos inválidos: "G500", "4 Gg", "abcKg", "123" (sem unidade)
        """
        if peso == "":
            raise ValueError("Campo peso está vazio")

        if not isinstance(peso, str):
            raise ValueError("Peso Inválido")

        s = peso.strip()

        # ^...$ garante que toda a string deve casar (sem sobras)
        padrao = re.compile(r'^([+-]?\d+(?:[.,]\d+)?)\s*(kg|g|ml|l)$', re.IGNORECASE)
        verificar = padrao.fullmatch(s)
        if not verificar:
            raise ValueError("Formato de peso inválido")

        numero_string = verificar.group(1).replace(',', '.')
        try:
            numero = float(numero_string)
        except ValueError:
            return False

        return numero > 0


    @staticmethod
    def validar_tamanho_vestuario(tamanho):
        """Faz a validação do tamanho de roupa ou calçado"""

        if tamanho == "":
            raise ValueError("Campo Tamanho está vazio")

        if tamanho.upper() in ["P", "M", "G", "GG"]:
            return True

        elif tamanho.isdigit():
            return True
        else:
            raise ValueError("Campo Tamanho está inválido")


