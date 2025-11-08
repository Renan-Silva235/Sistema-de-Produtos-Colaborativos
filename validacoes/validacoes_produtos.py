import re
from datetime import datetime


class ValidacoesProdutos:
    """
    Classe responsável por validar dados de produtos.

    Contém métodos estáticos para validar cadastro de produtos, formato de data,
    peso, tamanho de vestuário e outras validações relacionadas a produtos.
    """

    @staticmethod
    def validar_cadastro_produto(_caminho_arquivo, objeto, consulta):
        """
        Verifica se o produto já está cadastrado no sistema baseado na categoria e campos específicos.

        Para cada categoria (Alimentícios, Medicamentos, Vestuário), compara os campos relevantes
        do objeto fornecido com os produtos já cadastrados na lista de consulta.

        :param _caminho_arquivo: Caminho do arquivo JSON (não utilizado, mantido para compatibilidade)
        :param objeto: Dicionário com os dados do produto a ser verificado. Deve conter 'categoria'
                      e os campos específicos da categoria:
                      - Alimentícios: nome_alimento, peso, validade
                      - Medicamentos: nome_medicamento, dosagem, validade
                      - Vestuário: nome_produto, marca, cor, tamanho
        :param consulta: Lista de dicionários com os produtos já cadastrados no sistema
        :return: ID do produto se já estiver cadastrado, False caso contrário
        """

        regras = {
            "Alimentícios": ["nome_alimento", "peso", "validade"],
            "Medicamentos": ["nome_medicamento", "dosagem", "validade"],
            "Vestuário": ["nome_produto", "marca", "cor", "tamanho"],
        }

        categoria = objeto.get("categoria")
        campos = regras.get(categoria)
        if not campos:
            return False

        for consultado in consulta:
            if consultado.get("categoria") != categoria:
                continue

            if all(consultado.get(campo) == objeto.get(campo) for campo in campos):
                return consultado["id"]

        return False


    @staticmethod
    def validar_formato_data(data):
        """
        Valida se a string de data está no formato correto (dd/mm/aaaa).

        :param data: String com a data a ser validada no formato dd/mm/aaaa
        :return: True se a data estiver no formato correto
        :raises ValueError: Se a data não estiver no formato dd/mm/aaaa
        """
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
        """
        Valida se o tamanho de vestuário está no formato correto.

        Aceita tamanhos de roupas (P, M, G, GG) ou números para calçados.

        :param tamanho: String com o tamanho a ser validado
        :return: True se o tamanho for válido
        :raises ValueError: Se o tamanho estiver vazio ou não corresponder aos formatos aceitos
        """

        if tamanho == "":
            raise ValueError("Campo Tamanho está vazio")

        if tamanho.upper() in ["P", "M", "G", "GG"]:
            return True

        elif tamanho.isdigit():
            return True
        else:
            raise ValueError("Campo Tamanho está inválido")


